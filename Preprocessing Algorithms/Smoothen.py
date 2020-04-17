#https://stackoverflow.com/questions/46633544/smoothing-out-curve-in-python
#!/usr/bin/env python
import cv2
import numpy as np
import matplotlib.pyplot as plt
#from scipy.interpolate import spline
import math
import matplotlib
import os

#import matplotlib.axes.Axes.legend
#import matplotlib.pyplot.legend


lst=[]
dict={}
dict2={}

def smoothening(imageDir,imagePath):

    name = imageDir+"/noise_removed/"
    filenames= os.listdir(name)
    print(filenames)
    # if not os.path.exists(imageDir+"/smoothened/"):
    #     os.mkdir(imageDir+"/smoothened/")
    if not os.path.exists(imageDir+"/graph/"):
        os.mkdir(imageDir+"/graph/")

    for file in filenames:
        # a = os.path.join(subdir,file)
        # print(a)
        img = cv2.imread(name+file,0)

        #img = cv2.imread(a)
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        height, width = img.shape
        print(height,width)
        xdata = []
        ydata=[]

        for i in range(height):     
            for j in range(width):
                if(img[i][j]>40):   
                    img[i][j]=255
            else:
                img[i][j]=0

        for i in range(height):
            for j in range(width):
                if(img[i][j]==255):
                    xdata.append(i)
                    ydata.append(j)

        plt.figure()
        poly = np.polyfit(xdata,ydata,3)
        poly_y = np.poly1d(poly)(xdata)
        print(poly_y)
        plt.plot(xdata,poly_y)
        plt.plot(xdata,ydata)
        plt.plot(xdata,poly_y, "-b", label='smoothened')
        plt.xlabel('pixels')
        plt.ylabel('pixels')
        plt.plot(xdata,ydata, "-r", label='original')
        plt.legend(loc="upper left")
        plt.savefig(imageDir+"/graph/"+file)
        #plt.show()

        distance = 0
        for count in range(1,len(poly_y)):
            distance += math.sqrt(math.pow(xdata[count]-xdata[count-1],2) + math.pow(poly_y[count]-poly_y[count-1],2))
        # print("length is",distance)
        distance = float("{:.2f}".format(distance))
        print("length is",distance)
        lst.append(distance)
        dict.update({file:distance})

    lst.sort()
    print(lst)
    print(dict)
    print(sorted(dict.items(), key = 
                 lambda kv:(kv[1], kv[0])))
    return lst,dict