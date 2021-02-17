#Imports
import PIL
import PIL.Image as Img
import numpy as np
from scipy import ndimage

class RotateImage(object):
    '''
        Rotates the image about the centre of the image.
    '''

    def __init__(self, degrees):
        '''
            Arguments:
            degrees: rotation degree.
        '''
        
        # Write your code here
        self.angle = degrees

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

        image = ndimage.rotate(image,-1*self.angle,reshape = True)
        return image

