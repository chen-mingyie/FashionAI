from tensorflow.keras.models import load_model
from numpy.random import randn
from PIL import Image
import numpy as np
import tensorflow as tf

class articleGenerator():
    def __init__(self):
        # self.model = load_model("app/business/RGB_asy_generator_249.h5")

        # Load the TFLite model and allocate tensors.
        self.interpreter = tf.lite.Interpreter(model_path='app/business/RGB_asy_generator_249.tflite')
        self.interpreter.allocate_tensors()

    def generate_latent_points(self, latent_dim: int, n_samples: int):
        # generate points in the latent space
        x_input = randn(latent_dim * n_samples)
        # reshape into a batch of inputs for the network
        x_input = x_input.reshape(n_samples, latent_dim)
        return x_input

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

    def generateImages(self, nbrToGen: int=8) -> []:
        # Get input and output tensors.
        input_details = self.interpreter.get_input_details()
        output_details = self.interpreter.get_output_details()

        images = []
        for i in range(8):
            # Test the model on random input data.
            input_data = self.generate_latent_points(200, 1).astype(np.float32)
            self.interpreter.set_tensor(input_details[0]['index'], input_data)

            self.interpreter.invoke()

            # The function `get_tensor()` returns a copy of the tensor data.
            # Use `tensor()` in order to get a pointer to the tensor.
            output_data = self.interpreter.get_tensor(output_details[0]['index'])
            img_array = (output_data[0] * 127.5) + 127.5
            img = Image.fromarray(img_array.astype(np.uint8), 'RGB')
            images.append(img)
            img.save('app/static/img/generated/' + str(i) + '.jpg')

        return images