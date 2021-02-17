#Imports
from PIL import Image
import numpy as np
import os
#from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms = None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self.annotation_filepath = annotation_file
        self.transforms = transforms
        

    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        file = open(self.annotation_filepath,'r')
        count = 0
        for line in file:
            count += 1
        return count
        

    def __getitem__(self, idx):
        '''
            return the dataset element for the index: "idx"
            Arguments:
                idx: index of the data element.

            Returns: A dictionary with:
                image: image (in the form of a numpy array) (shape: (3, H, W))
                gt_bboxes: N X 5 array where N is the number of bounding boxes, each 
                            consisting of [class, x1, y1, x2, y2]
                            x1 and x2 lie between 0 and width of the image,
                            y1 and y2 lie between 0 and height of the image.

            You need to do the following, 
            1. Extract the correct annotation using the idx provided.
            2. Read the image and convert it into a numpy array (wont be necessary
                with some libraries). The shape of the array would be (3, H, W).
            3. Scale the values in the array to be with [0, 1].
            4. Create a dictonary with both the image and annotations
            4. Perform the desired transformations.
            5. Return the transformed image and annotations as specified.
        '''
        file = open(self.annotation_filepath,'r')
        count = 0
        for line in file:
            if count == idx:
                res = line
                break
            count += 1
        
        res_dict = eval(res)
        #image_path = '../../data/' + res_dict['img_fn']
        image_path = os.path.join(os.path.dirname(self.annotation_filepath), res_dict['img_fn'])
        image = Image.open(image_path)
        
        if self.transforms != None:
            for tf in self.transforms:
                image = tf(image)
        
        np_image = np.asarray(image)
        np_image = np_image.astype('float32')
        np_image = np_image/255.0
        np_image = np.transpose(np_image,(2,0,1))

        final_dict = dict()
        final_dict['image'] = np_image
        final_dict['gt_bboxes'] = []

        for box in res_dict['bboxes']:
            temp = []
            temp.append(box['category'])
            for z in box['bbox']:
                temp.append(z)

            final_dict['gt_bboxes'].append(temp)

        return final_dict



#ds = Dataset('../../data/annotations.jsonl',[CropImage((200,200))])
#file = open('temp.txt','w')
#file.write(str(ds[1]))
#print(ds[1])

        