
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir

Image Transformation - Scaling /Resizing
- Scaling is just resizing of the image. using the OpenCv functioj  cv.resize()
- for enlarging .prefer INTER_LINEAR or INTER_CUBIC interpolation 
if shrinking prefer the INTER_AREA

"""


# import cv library
import cv2 as cv 
import numpy as np

# read image from computer
img = cv.imread("images/dog1.jpg") 

# show the Actual Image
cv.imshow("original" , img)

resized = cv.resize(img, None , fx=2 , fy=2 , interpolation=cv.INTER_CUBIC)
# show the Scaled up Image 
cv.imshow("Scaled up " , resized) ;


resized = cv.resize(img, None , fx=0.5 , fy=0.5 , interpolation=cv.INTER_AREA)
# show the Scaled down Image 
cv.imshow("Scaled down " , resized) ;
