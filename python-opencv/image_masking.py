
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir

Image Massking
- Mask is the process of hinding some portion of an image and to reveal some portions 
- it's a non destructive process of image editing
- in OpenCV , we can use the bitwise AND operator to archive masking 



"""


# import cv library
import cv2 as cv 
#import numpy as np

# read image from computer
img = cv.imread("images/monkey1.jpg") 
mask = cv.imread("images/left_circle.jpg") 

cv.imshow("Image" , img)
cv.imshow("Mask" , mask)


# perform the bitwise operation for masking 
mascked_image = cv.bitwise_and(img , mask)
cv.imshow("Mascked Image" , mascked_image)

