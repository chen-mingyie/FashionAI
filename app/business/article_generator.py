from tensorflow.keras.models import load_model
from numpy.random import randn
from PIL import Image
import numpy as np
import tensorflow as tf

class articleGenerator():
    def __init__(self):
        # self.model = load_model("app/business/RGB_asy_generator_249.h5")

        # Load the TFLite model and allocate tensors.
        self.itpr_women_A = tf.lite.Interpreter(model_path='app/business/RGB_asy_generator_549.tflite')
        self.itpr_women_A.allocate_tensors()
        self.itpr_women_B = tf.lite.Interpreter(model_path='app/business/zalando-wms-wgb_asy_deep_generator_1599.tflite')
        self.itpr_women_B.allocate_tensors()
        self.itpr_men = tf.lite.Interpreter(model_path='app/business/zalando-wbg_asy_deep_generator_1049.tflite')
        self.itpr_men.allocate_tensors()

    def generate_latent_points(self, latent_dim: int, n_samples: int):
        # generate points in the latent space
        x_input = randn(latent_dim * n_samples)
        # reshape into a batch of inputs for the network
        x_input = x_input.reshape(n_samples, latent_dim)
        return x_input

    def generateImages(self, nbrToGen: int=8, style: str='women-style-A') -> []:
        # Get input and output tensors.
        if style == 'women-style-A':
            intepreter = self.itpr_women_A
        elif style == 'women-style-B':
            intepreter = self.itpr_women_B
        else:
            intepreter = self.itpr_men
        input_details = intepreter.get_input_details()
        output_details = intepreter.get_output_details()
        latentpts = input_details[0]['shape'][1]

        images = []
        for i in range(nbrToGen):
            # Test the model on random input data.
            input_data = self.generate_latent_points(latentpts, 1).astype(np.float32)
            intepreter.set_tensor(input_details[0]['index'], input_data)

            intepreter.invoke()

            # The function `get_tensor()` returns a copy of the tensor data.
            # Use `tensor()` in order to get a pointer to the tensor.
            output_data = intepreter.get_tensor(output_details[0]['index'])
            # if style == 'women-style-B':
            #     output_half1 = output_data[:, :, 0:int(output_data.shape[2] / 2), :]
            #     output_data = np.concatenate((output_half1, np.flip(output_half1, axis=2)), axis=2)
            img_array = (output_data[0] * 127.5) + 127.5
            img = Image.fromarray(img_array.astype(np.uint8), 'RGB')
            images.append(img)
            img.save('app/static/img/generated/' + str(i) + '.jpg')

        return images

    # def generateImages(self, nbrToGen: int=8) -> []:
    #     latent_points = self.generate_latent_points(200, nbrToGen)
    #     # generate images
    #     images = []
    #     X = self.model.predict(latent_points)
    #     for i in range(X.shape[0]):
    #         img_array = (X[i] * 127.5) + 127.5
    #         img = Image.fromarray(img_array.astype(np.uint8), 'RGB')
    #         images.append(img)
    #         img.save('app/static/img/generated/' + str(i) + '.jpg')
    #
    #     return images