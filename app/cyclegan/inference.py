"""Translate an image to another image
An example of command-line usage is:
python export_graph.py --model pretrained/apple2orange.pb \
                       --input input_sample.jpg \
                       --output output_sample.jpg \
                       --image_size 256
"""

import tensorflow as tf

# config = tf.compat.v1.ConfigProto(gpu_options=tf.compat.v1.GPUOptions(allow_growth=True))
# sess = tf.compat.v1.Session(config=config)


FLAGS = tf.compat.v1.flags.FLAGS
tf.compat.v1.flags.DEFINE_string('model_long', './app/cyclegan/pretrained/shirt2long.pb', 'model path (.pb)')
tf.compat.v1.flags.DEFINE_string('model_shirt', './app/cyclegan/pretrained/long2shirt.pb', 'model path (.pb)')

# tf.compat.v1.flags.DEFINE_string('model', './app/cyclegan/pretrained/long2shirt.pb', 'model path (.pb)')
tf.compat.v1.flags.DEFINE_string('input', './app/static/img/human-style-A.jpg', 'input image path (.jpg)')
tf.compat.v1.flags.DEFINE_string('output', './app/static/img/human-style-B.jpg', 'output image path (.jpg)')
tf.compat.v1.flags.DEFINE_integer('image_size', '256', 'image size, default: 256')

def convert2float(image):
  """ Transfrom from int image ([0,255]) to float tensor ([-1.,1.])
  """
  image = tf.image.convert_image_dtype(image, dtype=tf.float32)
  return (image/127.5) - 1.0


def inference(target_domain):

  graph = tf.compat.v1.Graph()

  with graph.as_default():
    with tf.compat.v1.gfile.FastGFile(FLAGS.input, 'rb') as f:
      image_data = f.read()
      input_image = tf.compat.v1.image.decode_jpeg(image_data, channels=3)
      input_image = tf.compat.v1.image.resize_images(input_image, size=(FLAGS.image_size, FLAGS.image_size))
      input_image = convert2float(input_image)
      input_image.set_shape([FLAGS.image_size, FLAGS.image_size, 3])

    if target_domain == 'long-sleeve':
      with tf.compat.v1.gfile.FastGFile(FLAGS.model_long, 'rb') as model_file:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(model_file.read())
      [output_image] = tf.compat.v1.import_graph_def(graph_def,
                            input_map={'input_image': input_image},
                            return_elements=['output_image:0'],
                            name='output')
    elif target_domain == 'shirt':
      with tf.compat.v1.gfile.FastGFile(FLAGS.model_shirt, 'rb') as model_file:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(model_file.read())
      [output_image] = tf.compat.v1.import_graph_def(graph_def,
                                                     input_map={'input_image': input_image},
                                                     return_elements=['output_image:0'],
                                                     name='output')

  with tf.compat.v1.Session(graph=graph) as sess:
    generated = output_image.eval()
    with open(FLAGS.output, 'wb') as f:
      f.write(generated)

# def main(unused_argv):
#   inference()
#
# if __name__ == '__main__':
#   tf.app.run()
