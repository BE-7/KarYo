import cv2
import numpy as np
import os


def skeleton(imageDir,imagePath):

	name = imageDir+"/connectedComponents/"
	filenames= os.listdir(name)
	print(filenames)

	for file in filenames:
		img = cv2.imread(name+file,0)
		#img = cv2.imread('Connected/'+z,0)
		#img = cv2.imread('images/cropped/2.jpg',0)
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
		#cv2.imshow("skel",skel)
		#cv2.imwrite("./skeleton/"+str(z), skel)


		#cv2.waitKey(0)
		# median = cv2.medianBlur(skel,3)
		# cv2.imshow("skel",median)
		# cv2.waitKey(0)
		#cv2.destroyAllWindows()
		if not os.path.exists(imageDir+"/skeleton/"):
			os.mkdir(imageDir+"/skeleton/")
		cv2.imwrite(imageDir+"/skeleton/"+str(file), skel)
		#cv2.imwrite("validation_result/"+directory+"/skeleton/"+str(file), skel)
		#cv2.imshow('image',img)
		#cv2.waitKey(0)
		cv2.destroyAllWindows()