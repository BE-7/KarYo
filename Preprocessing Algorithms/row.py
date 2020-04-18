import cv2
import numpy as np
import PIL
import sys
from PIL import Image, ImageDraw
from concat import concat
def row(lst,target):

	# t = imagePath.split("/")
	# imageDir = t[0]+"/"+t[1]+"/"+t[2]+"/"+t[3]+"/" 
	path = target+"/Resized/vertical"
	print("##########")
	print(lst)
	A = []
	B = []
	C = []
	D = []  

	#lst = [('43.jpg', 3.236067977499777), ('33.jpg', 7.071067811865483), ('41.jpg', 10.964724878577353), ('46.jpg', 12.034999410188222), ('31.jpg', 12.42723722081092), ('36.jpg', 13.17881648958412), ('26.jpg', 14.587319925722593), ('20.jpg', 14.882824613967331), ('34.jpg', 17.45929849618171), ('45.jpg', 17.990176050687683), ('23.jpg', 18.30835512550115), ('17.jpg', 18.56110321786805), ('22.jpg', 18.637345388044217), ('38.jpg', 18.734204403865945), ('14.jpg', 20.2921628262268), ('35.jpg', 21.49734604545561), ('40.jpg', 21.934712330176136), ('37.jpg', 22.624561243389792), ('30.jpg', 22.87916646860505), ('5.jpg', 24.42346214554805), ('44.jpg', 27.695265004878895), ('9.jpg', 27.94202675370851), ('39.jpg', 28.432097519840912), ('18.jpg', 29.532901616576865), ('6.jpg', 31.29894847906794), ('19.jpg', 33.24958456876382), ('12.jpg', 33.4073821587324), ('29.jpg', 33.90908243369089), ('28.jpg', 37.54283981688735), ('32.jpg', 39.49442544603043), ('24.jpg', 39.63496546878376), ('25.jpg', 41.44939319582502), ('7.jpg', 42.836499520552934), ('8.jpg', 42.84934761355323), ('11.jpg', 44.0752049627969), ('4.jpg', 44.338105647958194), ('13.jpg', 44.53810290119516), ('16.jpg', 47.44687380130529), ('3.jpg', 49.38592789078901), ('10.jpg', 49.53932107566584), ('2.jpg', 49.72443909046185), ('15.jpg', 53.7317540349579), ('21.jpg', 65.05739786074896), ('27.jpg', 67.50474637686915), ('1.jpg', 73.56442943155982), ('42.jpg', 104.4383612537255)]

	#st.reverse()
	#print(len(lst))

	#path = "G:/Karyotyping/Classifier/images/resized"
	for i in range(10):
		A.append(path+"/"+lst[i])
	for i in range(10,24):
		#print(i)
		B.append(path+"/"+lst[i])
	for i in range(24,36):
		C.append(path+"/"+lst[i])
	for i in range(36,len(lst)):
		#print(i)
		D.append(path+"/"+lst[i])


	#for image 1
	images = [Image.open(x) for x in A]
	widths, heights = zip(*(i.size for i in images))

	total_width = sum(widths) + 100
	max_height = max(heights) + 10
	new_im = Image.new('RGB', (total_width, max_height))

	x_offset = 0
	flag = 0
	for im in images:
		new_im.paste(im, (x_offset+10, 10))
		if flag%2==0:  
			temp_x = x_offset
			x_offset += im.size[0] - 30
		else:
			img1 = ImageDraw.Draw(new_im)   
			img1.rectangle([(temp_x+10, 10),(x_offset+10 + im.size[0], im.size[1]+10)], outline = "white", width = 2)
			x_offset += im.size[0] + 50
		flag+=1


	new_im.save(target+'/row1.jpg')



	#for image 2
	images = [Image.open(x) for x in B]
	widths, heights = zip(*(i.size for i in images))


	total_width = sum(widths) + 100
	max_height = max(heights) + 10

	new_im = Image.new('RGB', (total_width, max_height))

	x_offset = 0
	flag = 0
	for im in images:
		new_im.paste(im, (x_offset+10, 10))
		if flag%2==0:  
			temp_x = x_offset
			x_offset += im.size[0] - 30
		else:
			img1 = ImageDraw.Draw(new_im)   
			img1.rectangle([(temp_x+10, 10),(x_offset+10 + im.size[0], im.size[1]+10)], outline = "white", width = 2)
			x_offset += im.size[0] + 50
		flag+=1

	new_im.save(target+'/row2.jpg')


	#for image 3
	images = [Image.open(x) for x in C]
	widths, heights = zip(*(i.size for i in images))


	total_width = sum(widths) + 100
	max_height = max(heights) + 10

	new_im = Image.new('RGB', (total_width, max_height))

	x_offset = 0
	flag = 0
	for im in images:
		new_im.paste(im, (x_offset+10, 10))
		if flag%2==0:  
			temp_x = x_offset
			x_offset += im.size[0] - 30
		else:
			img1 = ImageDraw.Draw(new_im)   
			img1.rectangle([(temp_x+10, 10),(x_offset+10 + im.size[0], im.size[1]+10)], outline = "white", width = 2)
			x_offset += im.size[0] + 50
		flag+=1

	new_im.save(target+'/row3.jpg')


	#for image 4
	images = [Image.open(x) for x in D]
	widths, heights = zip(*(i.size for i in images))

	total_width = sum(widths) + 100
	max_height = max(heights) + 10

	new_im = Image.new('RGB', (total_width, max_height))

	x_offset = 0
	flag = 0
	for im in images:
		new_im.paste(im, (x_offset+10, 10))
		if flag%2==0:  
			temp_x = x_offset
			x_offset += im.size[0] - 30
		else:
			img1 = ImageDraw.Draw(new_im)   
			img1.rectangle([(temp_x+10, 10),(x_offset+10 + im.size[0], im.size[1]+10)], outline = "white", width = 2)
			x_offset += im.size[0] + 50
		flag+=1


	new_im.save(target+'/row4.jpg')

	concat(target)