
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir
https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html

Histogram equalization 

Used to improve the contrast of our images 
It stretches this histogram to either ends which improves the contrats of the image 
it is very useful for enhancinf scientific images like thermal , satelitte n space telescope or x-ray images 

Using the OpenCv function cv.equalizeHist()
Input a grayscale images and it will return the histogrma equalizd image   


plot == terrain 

"""


# import cv library
import cv2 as cv 


# read the image from computer
img = cv.imread("images/beach.jpg" ,0) 
cv.imshow("Original Image" , img )

#perform equalization 
corrected_img =  cv.equalizeHist(img)
cv.imshow("Equalized Image" , corrected_img )