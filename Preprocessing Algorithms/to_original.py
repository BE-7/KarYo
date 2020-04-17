import cv2
import numpy as np
import os

def to_original(imageDir,imagePath):

	name1 = imageDir+"/cropped/"
	name2 = imageDir+"/connectedComponents/"
	filenames= os.listdir(name1)
	print(filenames)

	for file in filenames:
		img = cv2.imread(name1+file,0)
		img2 = cv2.imread(name2+file,0)
		#img = cv2.imread('original/'+z,0)
		dest = cv2.bitwise_and(img,img2,mask=None)
		if not os.path.exists(imageDir+"/Original_after_max/"):
			os.mkdir(imageDir+"/Original_after_max/")
		cv2.imwrite(imageDir+"/Original_after_max/"+str(file), dest)
		
		#cv2.imwrite("./Original_after_max/"+str(z), dest)