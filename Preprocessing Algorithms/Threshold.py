import numpy as np
import cv2
import os

def threshold(imageDir,imagePath):

	name = imageDir+"/cropped/"
	filenames= os.listdir(name)
	print(filenames)

	#name = "validation_result"
	# dir_names = os.listdir(name)
	# print(dir_names)

	# for directory in dir_names:
	# 	filenames = os.listdir("validation_result/"+directory+"/cropped/")
	# 	#print(filenames)
	# 	if not os.path.exists("validation_result/"+directory+"/threshold"):
	# 		os.mkdir("validation_result/"+directory+"/threshold")
	for file in filenames:
		img = cv2.imread(name+file,0)
		#img=cv2.imread('1.jpg')
		width=img.shape[1]
		height=img.shape[0]
		dimensions=img.shape
		#print(dimensions)
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
		#cv2.imwrite('cropped_threshold.jpg',img)
		if not os.path.exists(imageDir+"/threshold/"):
			os.mkdir(imageDir+"/threshold/")
		cv2.imwrite(imageDir+"/threshold/"+str(file), img)
		#cv2.imshow('image',img)
		#cv2.waitKey(0)
		cv2.destroyAllWindows()