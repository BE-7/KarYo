#Importing required packages

from Threshold import threshold
from MaxConnectedComponents import maxCC
from Skeleton import skeleton
from Noise import noise
from Smoothen import smoothening
from to_original import to_original
from tilt import vertical
from resize import resize

def pre_process(imageDir):

	threshold(imageDir)
	resize(imageDir,"threshold")
	maxCC(imageDir)
	resize(imageDir,"connectedComponents")
	skeleton(imageDir)
	resize(imageDir,"skeleton")	
	noise(imageDir)
	resize(imageDir,"noise_removed")
	to_original(imageDir)
	resize(imageDir,"Original_after_max")
	vertical(imageDir)
	resize(imageDir,"vertical")
	lst,dict = smoothening(imageDir)
	print(lst)
	print(dict)
	return dict

#Uncomment the below line to test the module
#pre_process("G:/Karyotyping/chromosome_data/original 32/original 32.jpg","G:/Karyotyping/chromosome_data/original 32")