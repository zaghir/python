
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir
https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html

Image Pyramid

Creating set of images with different resolution 

Sametimes ,we may need images in diffent resolutions of the same base image 
The set of images with different resolutions are called Image Pyramids
Kept in a stack with the highst resolution image at the bottom and the lowest at top , like a pyramid
Using the OpenCV function cv.pyDown() to down sample and cv.pyrUp() to up sample



"""


# import cv library
import cv2 as cv 


# read the image from computer
img = cv.imread("images/cat1.jpg" ) 
cv.imshow("Original Image" , img )

#up sample pyramid 
up1 =  cv.pyrUp(img)
cv.imshow("up1 Image" , up1 )
up2 =  cv.pyrUp(up1)
cv.imshow("up1 Image" , up2 )
up3 =  cv.pyrUp(up2)
cv.imshow("up3 Image" , up3 )

#down sample pyramid
down1 =cv.pyrDown(img)
cv.imshow("down1 Image" , down1)
down2 =cv.pyrDown(down1)
cv.imshow("down2 Image" , down2)
