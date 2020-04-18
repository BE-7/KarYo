import numpy as np
import cv2
import os

def threshold(imageDir):

	name = imageDir+"/cropped/"
	filenames= os.listdir(name)
	for file in filenames:
		
		img = cv2.imread(name+file,0)
		width=img.shape[1]
		height=img.shape[0]
		dimensions=img.shape
		threshold=35

		#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		for i in np.arange(height):
		    for j in np.arange(width):
		        a=img[i][j]
		        if a>threshold:
		            b=255
		        if a<threshold:
		            b=0
		        img.itemset((i,j),b)

		if not os.path.exists(imageDir+"/threshold/"):
			os.mkdir(imageDir+"/threshold/")
		cv2.imwrite(imageDir+"/threshold/"+str(file), img)
		cv2.destroyAllWindows()