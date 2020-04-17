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


def vertical(imageDir,imagePath):

	name = imageDir+"/Original_after_max/"
	filenames= os.listdir(name)
	print(filenames)

	for file in filenames:
		img = cv2.imread(name+file,0)

		#img = cv2.imread("14.jpg")
		#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		# Or a distorted blob:
		# X, y = datasets.make_blobs(n_samples=100, centers = [[0,0]])
		# distortion = [[0.6, -0.6], [-0.4, 0.8]]
		# theta = np.radians(20)
		# rotation = np.array(((math.cos(theta),-math.sin(theta)), (math.sin(theta), math.cos(theta))))
		# X =  np.dot(np.dot(X, distortion),rotation)
		# img = np.histogram2d(*X.T)[0] # > 0 ## uncomment for making the example binary

		rotated_img = verticalize_img(img)
		rotated_img = imutils.rotate_bound(rotated_img,180)
		# Plot the results
		#plt.matshow(img)
		#plt.title('Original')
		#cv2.imshow("hey there", rotated_img)
		#cv2.imwrite("14vertical.jpg", rotated_img)
		#cv2.waitKey(0)

		if not os.path.exists(imageDir+"/vertical/"):
			os.mkdir(imageDir+"/vertical/")
		cv2.imwrite(imageDir+"/vertical/"+str(file), rotated_img)

		#cv2.imwrite("./vertical/"+str(z), rotated_img)


		#cv2.waitKey(0)
		# median = cv2.medianBlur(skel,3)
		# cv2.imshow("skel",median)
		# cv2.waitKey(0)
		cv2.destroyAllWindows()



# Example data:
# img = cv2.imread("14.jpg")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Or a distorted blob:
# # X, y = datasets.make_blobs(n_samples=100, centers = [[0,0]])
# # distortion = [[0.6, -0.6], [-0.4, 0.8]]
# # theta = np.radians(20)
# # rotation = np.array(((math.cos(theta),-math.sin(theta)), (math.sin(theta), math.cos(theta))))
# # X =  np.dot(np.dot(X, distortion),rotation)
# # img = np.histogram2d(*X.T)[0] # > 0 ## uncomment for making the example binary

# rotated_img = verticalize_img(img)
# # Plot the results
# plt.matshow(img)
# plt.title('Original')
# cv2.imshow("hey there", rotated_img)
# cv2.imwrite("14vertical.jpg", rotated_img)
# cv2.waitKey(0)
