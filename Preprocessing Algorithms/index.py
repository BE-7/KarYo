from Threshold import threshold
from MaxConnectedComponents import maxCC
from Skeleton import skeleton
from Noise import noise
from Smoothen import smoothening
from to_original import to_original
from tilt import vertical
from resize2 import resize2
from resize import resize

def pre_process(imagePath):

	t = imagePath.split("/")
	imageDir = t[0]+"/"+t[1]+"/"+t[2]+"/"+t[3]+"/"
	print(imageDir)
	resize(imageDir,imagePath)
	threshold(imageDir,imagePath)
	maxCC(imageDir,imagePath)
	skeleton(imageDir,imagePath)
	noise(imageDir,imagePath)
	to_original(imageDir,imagePath)
	vertical(imageDir,imagePath)
	resize2(imageDir,imagePath)
	lst,dict = smoothening(imageDir,imagePath)
	print(lst)
	print(dict)
	#print("works")
	return dict

#pre_process("G:/Karyotyping/chromosome_data/original 32/original 32.jpg")