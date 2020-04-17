import cv2
import numpy as np
import os


def undesired_objects (image,file,imageDir):
    image = image.astype('uint8')
    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=4)
    sizes = stats[:, -1]

    max_label = 1
    max_size = sizes[1]
    for i in range(2, nb_components):
        if sizes[i] > max_size:
            max_label = i
            max_size = sizes[i]

    img2 = np.zeros(output.shape)
    img2[output == max_label] = 255
    #cv2.imshow("Biggest component", img2)
    #cv2.imwrite('max_conneced.jpg', img2)
    if not os.path.exists(imageDir+"/connectedComponents/"):
        os.mkdir(imageDir+"/connectedComponents/")
    cv2.imwrite(imageDir+"/connectedComponents/"+str(file), img2)

    #cv2.imwrite("validation_result/"+directory+"/connectedComponents/"+str(file), img2)


def maxCC(imageDir,imagePath):

    name = imageDir+"/threshold/"
    filenames= os.listdir(name)
    print(filenames)
    for file in filenames:
        img = cv2.imread(name+file,0)
        #img = cv2.imread('cropped_threshold.jpg')
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


        undesired_objects(img,file,imageDir)