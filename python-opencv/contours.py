# -*- coding: utf-8 -*-
"""

@author: abhilash
"""
#import opencv library
import cv2 as cv

#read the image from computer
img = cv.imread('images/rupiah.jpg')
img_original = img.copy()

#apply preprocessing, conver to gery, blur and threshold
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = cv.GaussianBlur(img, (15, 15), 0)
img = cv.Canny(img, 30, 170)
thresh, thresh_img = cv.threshold(img, 127, 255, 0)

#pass pre-processed image, Contour retrieval mode and Contour approximation 
#Will return back Detected contours and hierarchy (containing information about the image topology)
contours, hierarchy = cv.findContours(thresh_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

#pass image, contours, contourIdx (-1 means all), color, thickness
#contours will be drawn on the image  passed
cv.drawContours(img_original, contours, -1, (0,255,0), 3)

cv.imshow("Preprocessed Image", thresh_img)
cv.imshow("Contours Drawn on Original", img_original)

print('No of objects detected is {}'.format(len(contours)))
