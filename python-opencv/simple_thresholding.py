
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir
https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html

Image Thresholding Le seuillage d'image

Le seuillage d'image est la méthode la plus simple de segmentation d'image. À partir d'une image en niveau de gris, le seuillage d'image peut être utilisé pour créer une image comportant uniquement deux valeurs, noir ou blanc (monochrome)1.

Le seuillage d'image remplace un à un les pixels d'une image à l'aide d'une valeur seuil fixée (par exemple 123). Ainsi, si un pixel à une valeur supérieure au seuil (par exemple 150), il prendra la valeur 255 (blanc), et si sa valeur est inférieure (par exemple 100), il prendra la valeur 0 (noir).

La valeur du seuil peut être déterminée manuellement ou bien automatiquement à partir de l'histogramme.

it's a, image segmentation technique
for instance, in binary threshold. Only two states ar possible.
if the pixel value is smoller than the threshold.it is set to min value(0). otherwise it is set to maximum value(255)

Simple manual techniqye is which if the pixel value is smaller than the threshold.set it to 0 , elese 255(or the maximum value specified).
the function cv.threshold() is used, which returns two outputs, the threshold used and threshold image , the input arguments are : 
     -1 argunet us the source image(should be grayscaleif need to get proper binary)
     -2 arguments is the threshold value 
     -3 argument is the maximum value 
     -4 is the type of simple threshold to be used
the different types of thresholding are 
     - cv.TRESH_BINARY
     - cv.TRESH_BINARY_INV
     - cv.TRESH_TRUNC
     - cv.TRESH_TOZERO
     - cv.TRESH_TOZERO_INV

"""


# import cv library
import cv2 as cv 
#import numpy as np

# read the image from computer
img = cv.imread("images/brain_ct.jpg") 
cv.imshow("Original Image" , img)


# perform simple threshold
# cv.threshold( src , thesh , maxVal , type) 
thresh,thresh_img = cv.threshold(img , 130 , 255 , cv.THRESH_BINARY)
cv.imshow("simple threshold Image" , thresh_img)

