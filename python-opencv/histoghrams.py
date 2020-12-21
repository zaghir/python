
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir
https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html

Histograms are graphs with pixrl values(ranginf from 0 to 255) in X-axis and corresponding number of pixels in the image on Y-axis 

By checking the histogrma of an images ,we could get an idea about the contrast , brightnes , intensity etc of that image  

Calculate Histogram using Matplotlib

Matplotlib is a plotting library for python to plot graphs easily from data 
Matplotlib comes with a histogram plotting function: matplotlib.pyplot.hist()



plot == terrain 

"""


# import cv library
import cv2 as cv 
#import numpy as np
from matplotlib import pyplot as plt

# read the image from computer
img = cv.imread("images/shirt1.jpg" ,0) 
cv.imshow("Original Image" , img )


plt.hist(img.ravel() , 256 , [0,256])
plt.show