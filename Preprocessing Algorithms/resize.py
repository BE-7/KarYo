import cv2
import numpy as np
import sys
from PIL import Image
import os

def resize(imageDir,newFolder):


	name = imageDir+"/"+newFolder+"/"
	filenames= os.listdir(name)
	# print(filenames)

	max_w = 0
	max_h = 0
	for file in filenames:
		img = cv2.imread(name+file,0)
		width = img.shape[1]
		height = img.shape[0]
		if(height>max_h):
			max_h = height
		if(width>max_w):
			max_w = width
	print(max_h,max_w)

	for file in filenames:
		img = cv2.imread(name+file,0)
		img2 = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
		ht, wd , cc = img2.shape
		ww = max_w #300
		hh = max_h #300
		color = (0,0,0)
		result = np.full((hh,ww,cc), color, dtype=np.uint8)

		# compute center offset
		xx = (ww - wd) // 2
		yy = (hh - ht) // 2

		# copy img image into center of result image
		result[yy:yy+ht, xx:xx+wd] = img2

		if not os.path.exists(imageDir+"/Resized/"):
			os.mkdir(imageDir+"/Resized/")
		if not os.path.exists(imageDir+"/Resized/"+newFolder+"/"):
			os.mkdir(imageDir+"/Resized/"+newFolder+"/")
		cv2.imwrite(imageDir+"/Resized/"+newFolder+"/"+str(file), result)