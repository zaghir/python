# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:36:07 2020

@author: yzaghir
"""

# import cv library
import cv2 as cv 

# read the image from computer 
img = cv.imread("images/img-1.jpg" , 0) # 0=  gresqlimage niveau de gri

# print the shape of image
print(img.shape)

# write the image to computer
cv.imwrite('images/img-1-m.jpg',img)

#show the image 
cv.imshow("photo" , img)


