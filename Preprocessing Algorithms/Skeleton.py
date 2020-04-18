import cv2
import numpy as np
import os


def skeleton(imageDir):

	name = imageDir+"/connectedComponents/"
	filenames= os.listdir(name)
	# print(filenames)

	for file in filenames:
		img = cv2.imread(name+file,0)
		width=img.shape[1]
		print(width)
		height=img.shape[0]
		print(height)
		dimensions=img.shape
		threshold=40
		for i in np.arange(height):
		    for j in np.arange(width):
		        a=img.item(i,j)
		        if a>threshold:
		            b=255
		        if a<threshold:
		            b=0
		        img.itemset((i,j),b)
		size = np.size(img)
		skel = np.zeros(img.shape,np.uint8)
		element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
		done = False
		while( not done):
			eroded = cv2.erode(img,element)
			temp = cv2.dilate(eroded,element)
			temp = cv2.subtract(img,temp)
			skel = cv2.bitwise_or(skel,temp)
			img = eroded.copy()
			zeros = size - cv2.countNonZero(img)
			if zeros==size:
				done = True
		if not os.path.exists(imageDir+"/skeleton/"):
			os.mkdir(imageDir+"/skeleton/")
		cv2.imwrite(imageDir+"/skeleton/"+str(file), skel)
		cv2.destroyAllWindows()