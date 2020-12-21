
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir
https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html

Read made Filters -Median Blurring 
- This filtering is done by using the OpenCV function cv.medianBlur()
- Here, we take medial of all the pixels under the kernel area and the central element is replaced with this median value

- Best for removin salt-and-pepper noise in an image


Read made Filters -Bilateral Blurring 
- This filtering is done by using the OpenCV function cv.belateralFilter()
- Here , only those pixels with similar intensites to the central pixel are considered for blurring.So it preseves the edges
- The operation is slower compared to other filters
- Best for noises removal while keeping edes sharp

"""


# import cv library
import cv2 as cv 
#import numpy as np

# read image from computer
img = cv.imread("images/rough_edge_img.jpg") 
cv.imshow("Original Image" , img)


# perform gaussian Blur filtering
result = cv.blur(img , (5,5))
cv.imshow("Average Smooth Image" , result)


# perform gaussian Blur filtering
result = cv.GaussianBlur(img , (5,5), 0)
cv.imshow("Gaussian Smooth Image" , result)



# read image from computer
img = cv.imread("images/noisy_img.jpg") 
cv.imshow("Original Image" , img)

# perform median Blur filtering
result = cv.medianBlur(img , 5)
cv.imshow("Median Blur Smooth Image" , result)

# read image from computer
img = cv.imread("images/pixelated_img.jpg") 
cv.imshow("Original Image" , img)


# perform bilateral filtering
result = cv.bilateralFilter(img , 10 , 75 , 75)
cv.imshow("Bilateral Smooth Image" , result)

