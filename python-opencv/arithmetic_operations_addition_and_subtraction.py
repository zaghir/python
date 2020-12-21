
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
img1 = cv.imread("images/abhi2.jpg") 
img2 = cv.imread("images/flower1.jpg") 


#macke sur both images are same size before adding 
# pickup matrix of number from image
cropped_image1 = img1[60:200 , 50:200]
cropped_image2 = img2[60:200 , 50:200]

cv.imshow("cropped 1" , cropped_image1)
cv.imshow("cropped 2" , cropped_image2)

# adding the images 
added_image = cv.add(cropped_image1 , cropped_image2)
cv.imshow("Added Image" , added_image)

# adding the images 
subtracted_image = cv.subtract(cropped_image1 , cropped_image2)
cv.imshow("Subtracted Image" , subtracted_image)
