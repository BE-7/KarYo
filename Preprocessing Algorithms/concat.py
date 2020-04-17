import cv2
import numpy as np
import PIL
import sys
from PIL import Image, ImageDraw


def concat(imageDir):

	list_im = [imageDir+'row1.jpg', imageDir+'row2.jpg', imageDir+'row3.jpg',imageDir+'row4.jpg']
	imgs    = [ PIL.Image.open(i) for i in list_im ]
	# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
	min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
	# imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

	# # save that beautiful picture
	# imgs_comb = PIL.Image.fromarray(imgs_comb)
	# imgs_comb.save( 'karyotype.jpg' )    

	# for a vertical stacking it is simple: use vstack
	imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

	imgs_comb = PIL.Image.fromarray(imgs_comb)
	w, h = imgs_comb.size
	black = Image.new('RGB', (w+50, h+50))

	#img1 = ImageDraw.Draw(imgs_comb)   
	black.paste(imgs_comb, (10, 10))
	img1 = ImageDraw.Draw(black)
	img1.rectangle([(10, 10),(w+20 , h+20)], outline = "white", width = 2)

	black.save( imageDir+'karyotype.jpg' )