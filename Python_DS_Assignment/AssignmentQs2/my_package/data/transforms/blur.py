#Imports
import PIL
import PIL.Image as Img
from PIL import ImageFilter
import numpy as np

class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''

    def __init__(self, radius = 3):
        '''
            Arguments:
            radius (int): radius to blur
        '''

        # Write your code here
        self.radius = radius

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        '''

        # Write your code here
        if isinstance(image,np.ndarray):
            image = Img.fromarray(np.uint8(image)).convert('RGB')

        image = image.filter(ImageFilter.GaussianBlur(self.radius))
        return image
