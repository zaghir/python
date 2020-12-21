
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir

Read made Filters -Averaging 
- This filtering is done by using the OpenCV function cv.blur()
- Takes the average of all the pixels under the kernel area and replaces the center element


Read made Filters -Gaussian Blurring
- This filtering is  done by using the openCV fucntion cv.GaussianBlur()
- Here. instead of box filter , Gaussian kernel is used 

"""


# import cv library
import cv2 as cv 
import numpy as np

# read image from computer
img = cv.imread("images/rough_edge_img.jpg") 
cv.imshow("Original Image" , img)


# perform gaussian Blur filtering
result = cv.blur(img , (5,5))
cv.imshow("Average Smooth Image" , result)


# perform gaussian Blur filtering
result = cv.GaussianBlur(img , (5,5), 0)
cv.imshow("Gaussian Smooth Image" , result)



