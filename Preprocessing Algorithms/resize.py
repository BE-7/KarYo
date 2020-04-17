import cv2
import numpy as np
import sys
from PIL import Image
import os

def resize(imageDir,imagePath):


	name = imageDir+"/cropped/"
	filenames= os.listdir(name)
	print(filenames)

	#lst = [('43.jpg', 3.236067977499777), ('33.jpg', 7.071067811865483), ('41.jpg', 10.964724878577353), ('46.jpg', 12.034999410188222), ('31.jpg', 12.42723722081092), ('36.jpg', 13.17881648958412), ('26.jpg', 14.587319925722593), ('20.jpg', 14.882824613967331), ('34.jpg', 17.45929849618171), ('45.jpg', 17.990176050687683), ('23.jpg', 18.30835512550115), ('17.jpg', 18.56110321786805), ('22.jpg', 18.637345388044217), ('38.jpg', 18.734204403865945), ('14.jpg', 20.2921628262268), ('35.jpg', 21.49734604545561), ('40.jpg', 21.934712330176136), ('37.jpg', 22.624561243389792), ('30.jpg', 22.87916646860505), ('5.jpg', 24.42346214554805), ('44.jpg', 27.695265004878895), ('9.jpg', 27.94202675370851), ('39.jpg', 28.432097519840912), ('18.jpg', 29.532901616576865), ('6.jpg', 31.29894847906794), ('19.jpg', 33.24958456876382), ('12.jpg', 33.4073821587324), ('29.jpg', 33.90908243369089), ('28.jpg', 37.54283981688735), ('32.jpg', 39.49442544603043), ('24.jpg', 39.63496546878376), ('25.jpg', 41.44939319582502), ('7.jpg', 42.836499520552934), ('8.jpg', 42.84934761355323), ('11.jpg', 44.0752049627969), ('4.jpg', 44.338105647958194), ('13.jpg', 44.53810290119516), ('16.jpg', 47.44687380130529), ('3.jpg', 49.38592789078901), ('10.jpg', 49.53932107566584), ('2.jpg', 49.72443909046185), ('15.jpg', 53.7317540349579), ('21.jpg', 65.05739786074896), ('27.jpg', 67.50474637686915), ('1.jpg', 73.56442943155982), ('42.jpg', 104.4383612537255)]
	max_w = 0
	max_h = 0
	for file in filenames:
		img = cv2.imread(name+file,0)
		width = img.shape[1]
		height = img.shape[0]
		#print("dwvdjvwfjvw"+width+"vwehdvwefhvwvwjhed"+height)
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

		#cv2.imshow("result", result)
		#cv2.waitKey(0)

		# compute center offset
		xx = (ww - wd) // 2
		yy = (hh - ht) // 2

		# copy img image into center of result image
		result[yy:yy+ht, xx:xx+wd] = img2

		# view result
		#cv2.imshow("result", result)
		#cv2.imwrite("b.jpg", result)
		#cv2.waitKey(0)
		#cv2.resize(img,(max_w,max_h))
		#if not os.path.exists(imageDir+"/resized/"):
		#	os.mkdir(imageDir+"/resized/")
		cv2.imwrite(imageDir+"/cropped/"+str(file), result)
		# cv2.imwrite("./Resized/"+i[0], result)