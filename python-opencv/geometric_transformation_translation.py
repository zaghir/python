
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir

Image Transformation - Translation
Translation is defined as shifting of an object's location 
we can move the image to top , bottom, left , right , in indifidual direction or as combination of directions 

create the transformation matrix M = [1  0  tx which is a Numpy array of type np.float32
                                      0  1  ty]
txis the shift in x-axis . ty is the shift in y-axis 
Can use-ve as well as +ve value for tx and ty 
use transformation function cv.warpAffine()


"""


# import cv library
import cv2 as cv 
import numpy as np

# read image from computer
img = cv.imread("images/dog1.jpg") 

# show the Actual Image
cv.imshow("original" , img)

#define the transformation matrix
#trans_matrix = np.float32([[1,0,50] , [0,1,-25]])
trans_matrix = np.float32([[1,0,50] , [0,1,25]])

#shifting the image
shifted_image = cv.warpAffine(img , trans_matrix, (img.shape[1], img.shape[0]))
# show the Shifted Image
cv.imshow("Shifted" , shifted_image)

"""

"""