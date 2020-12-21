
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir

Image Arthmeric Opeations Add - 
We can add two images with the OpenCV function , cv.add()
-Resize the two images and make sur they are exactly the same size before adding 



"""


# import cv library
import cv2 as cv 
#import numpy as np

# read image from computer
img1 = cv.imread("images/left_circle.jpg") 
img2 = cv.imread("images/right_circle.jpg") 



cv.imshow("Image 1" , img1)
cv.imshow("Image 2" , img2)

# perform the bitwise operations 
result = cv.bitwise_and(img1 , img2)
cv.imshow("AND" , result)


result = cv.bitwise_or(img1 , img2)
cv.imshow("OR" , result)

result = cv.bitwise_xor(img1 , img2)
cv.imshow("XOR" , result)

result = cv.bitwise_not(img1 , img2)
cv.imshow("NOT" , result)

