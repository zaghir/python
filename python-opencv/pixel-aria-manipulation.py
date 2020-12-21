# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir
"""


# import cv library
import cv2 as cv 

# read the image from computer 
img = cv.imread("images/img-1.jpg") 

# print the shape of image
print(img.shape)

#get pixel at row , colum position 
pixel = img[120,120]
print("Color intensity at (120, 120) pixel is Blue: {}, Green: {} Red: {}".format(pixel[0], pixel[1], pixel[2]))

#get only single color value for pixel 
red_pixel = img[120,120,2] # 0 = bleu , 1 = green , 2 = red
print("Color intensity of red pixel at(120 , 120) is {}".format(red_pixel))

# set the color of pixel at 120x120 to green
img[120,120] = (0,250,0)
pixel = img[120,120]
print("Color intensity at (120, 120) pixel is Blue: {}, Green: {} Red: {}".format(pixel[0], pixel[1], pixel[2]))

#get the region from the image 
slice = img[0:120 , 0:120]
cv.imshow("sciced image ",slice )

# set the color of area at 120:0 till 0:120 to green
img[0:120 , 0:120] = (0,250,0)
pixel = img[120,120]
cv.imshow("manipulated slice of image ",img)

#printing properties of image 
print("shape of image")
print(img.shape)
print("total  no of pixels in the  image")
print(img.size)
print("data type of image")
print(img.dtype)

## video camera
##cap = cv.VideoCapture(0)
##while True :
 ##   ret ,frame = cap.read(0)
 ##   cv.imshow("Video Face Detect " ,frame)
 ##   k= cv.waitKey(1)
 ##   if k == 27:
 ##       break
##cap.release()
##cv.destroyAllWindows()
