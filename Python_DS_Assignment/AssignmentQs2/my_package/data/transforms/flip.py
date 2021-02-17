#Imports
import PIL
import PIL.Image as Img
import numpy as np

class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''

        # Write your code here
        self.flip_type = flip_type
        
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

        if self.flip_type == 'horizontal':
            image = np.fliplr(image)
            return image

        else: 
            image = np.flipud(image)
            return image
