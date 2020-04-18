from matplotlib import pyplot as plt
from scipy.ndimage.interpolation import rotate
#from skimage.transform import rotate ## Alternatively
from sklearn.decomposition.pca import PCA ## Or use its numpy variant
import numpy as np
from sklearn import cluster, datasets
import cv2 
import math
import os
import imutils

def verticalize_img(img):
    """
    Method to rotate a greyscale image based on its principal axis.

    :param img: Two dimensional array-like object, values > 0 being interpreted as containing to a line
    :return rotated_img: 
    """# Get the coordinates of the points of interest:
    X = np.array(np.where(img > 0)).T
    # Perform a PCA and compute the angle of the first principal axes
    pca = PCA(n_components=2).fit(X)
    angle = np.arctan2(*pca.components_[0])
    # Rotate the image by the computed angle:
    rotated_img = rotate(img,angle/math.pi*180-90)
    return rotated_img


def vertical(imageDir):

	name = imageDir+"/Original_after_max/"
	filenames= os.listdir(name)
	# print(filenames)

	for file in filenames:
		img = cv2.imread(name+file,0)

		# img = np.histogram2d(*X.T)[0] # > 0 ## uncomment for making the example binary

		rotated_img = verticalize_img(img)
		rotated_img = imutils.rotate_bound(rotated_img,180)

		if not os.path.exists(imageDir+"/vertical/"):
			os.mkdir(imageDir+"/vertical/")
		cv2.imwrite(imageDir+"/vertical/"+str(file), rotated_img)
		cv2.destroyAllWindows()