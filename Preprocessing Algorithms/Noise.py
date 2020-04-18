import cv2
import numpy as np
import os

def noise(imageDir):

	name = imageDir+"/skeleton/"
	filenames= os.listdir(name)
	# print(filenames)

	for file in filenames:
		img = cv2.imread(name+file,0)
		# load image, ensure binary, remove bar on the left
		input_image = img
		input_image = cv2.threshold(input_image, 254, 255, cv2.THRESH_BINARY)[1]
		input_image_comp = cv2.bitwise_not(input_image)  # could just use 255-img

		kernel1 = np.array([[0, 0, 0],
		                    [0, 1, 0],
		                    [0, 0, 0]], np.uint8)
		kernel2 = np.array([[1, 1, 1],
		                    [1, 0, 1],
		                    [1, 1, 1]], np.uint8)

		hitormiss1 = cv2.morphologyEx(input_image, cv2.MORPH_ERODE, kernel1)
		hitormiss2 = cv2.morphologyEx(input_image_comp, cv2.MORPH_ERODE, kernel2)
		hitormiss = cv2.bitwise_and(hitormiss1, hitormiss2)

		hitormiss_comp = cv2.bitwise_not(hitormiss)  # could just use 255-img
		del_isolated = cv2.bitwise_and(input_image, input_image, mask=hitormiss_comp)
		if not os.path.exists(imageDir+"/noise_removed/"):
			os.mkdir(imageDir+"/noise_removed/")
		cv2.imwrite(imageDir+"/noise_removed/"+str(file), del_isolated)
		cv2.destroyAllWindows()