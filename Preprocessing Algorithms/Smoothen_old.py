#https://stackoverflow.com/questions/46633544/smoothing-out-curve-in-python
import cv2
import numpy as np
import matplotlib.pyplot as plt
#from scipy.interpolate import spline
import math
import os


lst=[]
dict={}

def smoothening(imageDir,imagePath):

    name = imageDir+"/noise_removed/"
    filenames= os.listdir(name)
    print(filenames)
    if not os.path.exists(imageDir+"/smoothened/"):
        os.mkdir(imageDir+"/smoothened/")
    if not os.path.exists(imageDir+"/graph/"):
        os.mkdir(imageDir+"/graph/")
    for file in filenames:
        img = cv2.imread(name+file,0)
        height, width = img.shape
        print(height,width) #87,96
        xdata = []
        ydata=[]

        for i in range(height):     #x=87 y=96
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
        print(xdata)
        print(ydata)
        print(len(xdata))
        print(len(ydata))
        plt.figure()
        poly = np.polyfit(xdata,ydata,5)
        poly_y = np.poly1d(poly)(xdata)
        #plt.plot(xdata,poly_y)
        #plt.plot(xdata,ydata)
        
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
        distance = float("{:.2f}".format(distance))
        print("length is",distance)
        lst.append(distance)
        dict.update({file:distance})
        img2 = img
        for i in range(height):     #x=87 y=96
            for j in range(width):
                    img2[i][j]=0


        for i in range(len(xdata)):
            a=xdata[i]
            b=poly_y[i]
            img2[a][(int(math.floor(b)))]=255
            img2[a][(int(math.ceil(b)))]=255
        dest=cv2.bitwise_or(img2, img, mask = None) 
        #cv2.imshow("new", dest)
        #cv2.imwrite("./Graph/"+str(z),dest)

        cv2.imwrite(imageDir+"/smoothened/"+str(file), dest)
        # cv2.imwrite("validation_result/"+directory+"/smoothened/"+str(file), dest)
        cv2.destroyAllWindows()
        
    lst.sort()
    print(lst)
    print(dict)
    print(sorted(dict.items(), key = 
                 lambda kv:(kv[1], kv[0])))
    return lst,dict