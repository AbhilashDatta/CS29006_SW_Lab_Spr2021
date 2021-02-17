#Imports
from my_package.model import ObjectDetectionModel
from my_package.data import Dataset
from my_package.analysis import plot_boxes
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 

def experiment(annotation_file, detector, transforms = None, outputs = None):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        detector: The object detector
        transforms: List of transformation classes
        outputs: path of the output folder to store the images
    '''

    #Create the instance of the dataset.
    d = Dataset(annotation_file, transforms)

    #Iterate over all data items.
    for i in range(len(d)):

    #Get the predictions from the detector.
        pred = detector(d[i]['image'])

    #Draw the boxes on the image and save them.
        plot_boxes(outputs+str(i)+".png",d[i]['image'],pred)

    #Do the required analysis experiments.
    fp = "./outputs/"
    img1 = d[1]['image']
    pred = detector(img1)
    n_img = plot_boxes(fp + "original.png", img1, pred)
    plt.subplot(2,4,1)
    plt.imshow(n_img)
    plt.title("Original")

    d = Dataset(annotation_file,[FlipImage('horizontal')])
    img2 = d[1]['image']    
    pred = detector(img2)
    n_img = plot_boxes(fp + "flip.png", img2, pred)
    plt.subplot(2,4,2)
    plt.imshow(n_img)
    plt.title("Horizontally flip")

    d = Dataset(annotation_file,[BlurImage(3)])
    img3 = d[1]['image']    
    pred = detector(img3)
    n_img = plot_boxes(fp+"blur.png", img3, pred)
    plt.subplot(2,4,3)
    plt.imshow(n_img)
    plt.title("Blurred")

    d = Dataset(annotation_file,[RescaleImage((2*img3.shape[2],2*img3.shape[1]))])
    img4 = d[1]['image']
    pred = detector(img4)
    n_img = plot_boxes(fp + "2x.png", img4, pred)
    plt.subplot(2,4,4)
    plt.imshow(n_img)
    plt.title("2X")

    d = Dataset(annotation_file,[RescaleImage((round(0.5*img3.shape[2]),round(0.5*img3.shape[1])))])   
    img5 = d[1]['image']
    pred = detector(img5)
    n_img = plot_boxes(fp + "halfx.png", img5, pred)
    plt.subplot(2,4,5)
    plt.imshow(n_img)
    plt.title("0.5X")

    d = Dataset(annotation_file,[RotateImage(90)])
    img6 = d[1]['image']    
    pred = detector(img6)
    n_img = plot_boxes(fp + "90right.png", img6, pred)
    plt.subplot(2,4,6)
    plt.imshow(n_img)
    plt.title("90degree right")

    d = Dataset(annotation_file,[RotateImage(-45)])
    img7 = d[1]['image']    
    pred = detector(img7)
    n_img = plot_boxes(fp + "45left.png", img7, pred)
    plt.subplot(2,4,7)
    plt.imshow(n_img)
    plt.title("45degree left")
    plt.show()


def main():
    detector = ObjectDetectionModel()
    experiment('./data/annotations.jsonl', detector, [], "./outputs/") # Sample arguments to call experiment()


if __name__ == '__main__':
    main()