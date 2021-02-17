#Imports
import cv2
import numpy as np
from PIL import ImageDraw, Image

def Sort_Tuple(tup):  
	return(sorted(tup, key = lambda x: x[2],reverse = True))

def plot_boxes(output_location, image, pred): # Write the required arguments

	# The function should plot the predicted boxes on the images and save them.
	# Tip: keep the dimensions of the output image less than 800 to avoid RAM crashes.
	image = Image.fromarray((np.transpose(image,(1,2,0))*255).astype(np.uint8))
	#pred = zip(pred_boxes, pred_class, pred_score)
	n = len(pred[1])

	if n<=5:
		for i in range(n):
			text = pred[1][i]
			shape = pred[0][i]
			img = ImageDraw.Draw(image)
			img.text([shape[0][0],shape[1][1]],text)
			img.rectangle(shape, outline = 'red')
		image.save(output_location)
		return image

	else:
		i = 0
		while i<5:
			maxi = 0
			max = 0
			for j in range(n):
				if pred[2][j]>max:
					max = pred[2][j]
					maxi = j
			text = pred[1][maxi]
			shape = pred[0][maxi]
			img = ImageDraw.Draw(image)
			img.text([shape[0][0],shape[1][1]],text)
			img.rectangle(shape, outline = 'red')
			pred[2][maxi] = -2
			i+=1
		image.save(output_location)
		return image
		