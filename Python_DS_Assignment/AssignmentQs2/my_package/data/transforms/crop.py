#Imports
import PIL
import PIL.Image as Img
import numpy as np

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''

        # Write your code here
        self.shape = shape
        self.crop_type = crop_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        if not isinstance(image,np.ndarray):
            image = np.asarray(image)

        if self.crop_type == 'center': 
            x = image.shape[0]//2
            y = image.shape[1]//2
        else:
            x = np.random.randint(self.shape[0]//2,image.shape[0]-self.shape[0]//2)
            y = np.random.randint(self.shape[1]//2,image.shape[1]-self.shape[1]//2)

        start1 = x - self.shape[0]//2
        end1 = x + self.shape[0]//2
        start2 = y - self.shape[1]//2
        end2 = y + self.shape[1]//2
        #start3 = 0
        #end3 = 3
        image = image[start1:end1, start2:end2]#, start3:end3]
        return image

