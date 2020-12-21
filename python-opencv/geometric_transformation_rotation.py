
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir

Image Transformation - Rotation
Create the tranformation matrix using the function cv.getRotationMatrix2D()
Passin in the rotation pivot (centre mostly) points, rotation angle and scaling factor


"""


# import cv library
import cv2 as cv 
#import numpy as np

# read image from computer
img = cv.imread("images/dog1.jpg") 

# show the Actual Image
cv.imshow("original" , img)

#define the transformation matrix
#getRotationMatrix2D(centre , angle , scale)
trans_matrix = cv.getRotationMatrix2D((img.shape[1]//2 , img.shape[0]//2) , 75 , 1)

#rotated the image
#warpAffine(src , Matrix , dsize)
rotated_image = cv.warpAffine(img , trans_matrix, (img.shape[1], img.shape[0]))
# show the Shifted Image
cv.imshow("Rotated" , rotated_image)

"""

"""