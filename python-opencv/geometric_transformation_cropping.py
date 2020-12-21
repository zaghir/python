
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir

Image Transformation - Cropping  Recadrage

Cropping is the removal of unwanted outer areas from a photographic or illustrated image
Opencv understands images as NumPy arrays, We can so simple array slicing to get an image cropped


"""


# import cv library
import cv2 as cv 
#import numpy as np

# read image from computer
img = cv.imread("images/abhi2.jpg") 

# show the Actual Image
cv.imshow("original" , img)

# the 4 indexes are starty, endy, startx , endx
#make sure index fall insid the image widht an height and logically crop-able

cropped_image = img[60:200 , 50:200]
# show the Actual Image
cv.imshow("Cropped" , cropped_image)