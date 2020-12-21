# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir
"""


# import cv library
import cv2 as cv 
#import numpy as np

# read the image from computer 
img = cv.imread("images/dog1.jpg") 

#show the BGR image 
cv.imshow("BGR Color Space" , img)

#show the gray color space image 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray Color Space" , gray)


#show the gray color space image
# HSV => hue saturation value , is th measurements the is used to see how much intensity of color is there .Which somewhat is there
#       resembles to .. it does not have any solid prood but its actually belived to be this is how we perceive the color. 
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV Color Space" , hsv)

#show the gray color space image 
# LAB => L for dark to Light the variations of black till white
#        B is for blue till Yellow
#        A is for red
#        That is from Green to Red
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB Color Space" , lab)

