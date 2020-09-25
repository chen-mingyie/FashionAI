from keras.models import load_model
import tensorflow as tf
from PIL import Image
import numpy as np
from app.business.instance_normalization import InstanceNormalization
from random import randint
from tensorflow.python.keras.backend import set_session

class viton():

    def __init__(self):
        self.sess = tf.Session()
        self.graph = tf.get_default_graph()
        set_session(self.sess)
        self.gen_model = load_model("app/business/generator.h5",custom_objects={'InstanceNormalization':InstanceNormalization})
        self.isRGB = True
        self.apply_da = True
        self.channel_first = False

    def crop_img(self, img, large_size, small_size):
        img_width = small_size[0]
        img_height = small_size[1]
        diff_size = (large_size[0]-small_size[0], large_size[1]-small_size[1])
        
        x_range = [i for i in range(diff_size[0])]
        y_range = [j for j in range(diff_size[1])]
        x0 = np.random.choice(x_range)
        y0 = np.random.choice(y_range)
        
        img = np.array(img)
        
        img = img[y0: y0+img_height, x0: x0+img_width, :]
        
        return img

    def read_image(self):
        input_size = (111,148)
        cropped_size = (96,128)
       
        if self.isRGB:
        # Load human picture
            im = Image.open("app/static/img/human-article-A.jpg").convert('RGB')
            im = im.resize( input_size, Image.BILINEAR )    
        else:
            im = cv2.imread(fn)
            im = cv2.cvtColor(im, cv2.COLOR_BGR2LAB)
            im = cv2.resize(im, input_size, interpolation=cv2.INTER_CUBIC)
        if self.apply_da is True:
            im = self.crop_img(im, input_size, cropped_size)
        arr = np.array(im)/255*2-1
        img_x_i = arr
        if self.channel_first:        
            img_x_i = np.moveaxis(img_x_i, 2, 0)
            
        # Load article picture y_i
        y_i = "app/static/img/article-A.jpg"
        if self.isRGB:
            im = Image.open(y_i).convert('RGB')
            im = im.resize(cropped_size, Image.BILINEAR )    
        else:
            im = cv2.imread(y_i)
            im = cv2.cvtColor(im, cv2.COLOR_BGR2LAB)
            im = cv2.resize(im, cropped_size, interpolation=cv2.INTER_CUBIC)
        arr = np.array(im)/255*2-1
        img_y_i = arr
        if self.channel_first:        
            img_y_i = np.moveaxis(img_y_i, 2, 0)
        
        # Load article picture y_j randomly
        if self.isRGB:
            im = Image.open("app/static/img/article-B.jpg").convert('RGB')
            im = im.resize( cropped_size, Image.BILINEAR )
        else:
            im = cv2.imread("app/static/img/article-B.jpg")
            im = cv2.cvtColor(im, cv2.COLOR_BGR2LAB)
            im = cv2.resize(im, cropped_size, interpolation=cv2.INTER_CUBIC)
        arr = np.array(im)/255*2-1
        img_y_j = arr
        if randint(0,1): 
            img_y_j=img_y_j[:,::-1]
        if self.channel_first:        
            img_y_j = np.moveaxis(img_y_j, 2, 0)        
        
        if randint(0,1): # prevent disalign of the graphic on t-shirts and human when fplipping
            img_x_i=img_x_i[:,::-1]
            img_y_i=img_y_i[:,::-1]
        
        img = np.concatenate([img_x_i, img_y_i, img_y_j], axis=-1)    
        assert img.shape[-1] == 9
        
        return img
    
    def generate_new_image(self):
        img = [self.read_image()]
        img = np.float32(img)        
        image_model = img[:,:,:,:3]
        image_cloth = img[:,:,:,3:6]
        target_cloth = img[:,:,:,6:]
        fake_image=[]
        global graph
        global sess
        set_session(self.sess)
        with self.graph.as_default():
            fake_image = self.gen_model.predict(img)
            print(fake_image.shape)
        fake_image_alpha = fake_image[:,:,:,0:1]
        fake_image_model = fake_image[:,:,:,1:]
        fake_image_output = fake_image_alpha*fake_image_model + (1-fake_image_alpha)*image_model
        print(fake_image_output.shape)
        img_array = (fake_image_output[0] * 127.5) + 127.5
        final_image = Image.fromarray(img_array.astype(np.uint8), 'RGB')
        final_image.save('app/static/img/generated/human-article-B.jpg')