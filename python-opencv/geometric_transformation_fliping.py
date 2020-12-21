
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir

Image Transformation - Flipping

Using cv.flip() method
Pass image (input array) and the flip code(1-horizontal, 0-vertical, -1 both)


"""


# import cv library
import cv2 as cv 
#import numpy as np

# read image from computer
img = cv.imread("images/dog1.jpg") 

# show the Actual Image
cv.imshow("original" , img)

#fliped images
#warpAffine(src , Matrix , dsize)
flipped_image = cv.flip(img , 1)
# show the Shifted Image
cv.imshow("Flipped Horizontal" , flipped_image)

flipped_image = cv.flip(img , 0)
# show the Shifted Image
cv.imshow("Flipped Verical" , flipped_image)


flipped_image = cv.flip(img , -1)
# show the Shifted Image
cv.imshow("Flipped Both Directions" , flipped_image)

"""

"""