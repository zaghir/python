# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir
"""


# import cv library
import cv2 as cv 
import numpy as np

# read the image from computer 
img = cv.imread("images/shirt1.jpg") 

#show the image 
cv.imshow("shirt photo origne" , img)


# split the color channels 
blue ,green, red = cv.split(img) 

# show the blue pixel intensity
cv.imshow("blue pixel intensity",blue)

# show the green pixel intensity
cv.imshow("green pixel intensity",green)

# show the red pixel intensity
cv.imshow("red pixel intensity",red)

# merge the image color channels
img_merged = cv.merge((blue, green, red))

#show the merged image
cv.imshow("shirt1 photo merged" , img_merged)

# Display only single color channels 
# Import mumpy and create a zeros  array of the size of image 
# :2  all colum 1 until 2  ,  image.shape1 image.shape2  
zeros_array = np.zeros(img_merged.shape[:2],dtype="uint8")
red_only_image=cv.merge((zeros_array,zeros_array,red))

# show the red only channel image
cv.imshow("shirt1 red only channel image",red_only_image)

green_only_image=cv.merge((zeros_array,green,zeros_array))

# show the red only channel image
cv.imshow("shirt1 green only channel image",green_only_image)


blue_only_image=cv.merge((blue,zeros_array,zeros_array))

# show the red only channel image
cv.imshow("shirt1 blue only channel image",blue_only_image)


