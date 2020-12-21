
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir
https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html

En vision par ordinateur et traitement d'image, la méthode d'Otsu est utilisée pour effectuer un seuillage automatique à partir de la forme de l'histogramme de l'image1, ou la réduction d'une image à niveaux de gris en une image binaire. L'algorithme suppose alors que l'image à binariser ne contient que deux classes de pixels, (c'est-à-dire le premier plan et l'arrière-plan) puis calcule le seuil optimal qui sépare ces deux classes afin que leur variance intra-classe soit minimale2.
L'extension de la méthode originale pour faire du seuillage à plusieurs niveaux est appelée Multi Otsu method3. Le nom de cette méthode provient du nom de son initiateur, Nobuyuki Otsu (大津展之, Ōtsu Nobuyuki?). Elle ne doit pas être confondue avec la méthode d'Antzu.

Utsu's method determinses an optimal global threshold value from the image histogram
here the simple cv.threshold() function is used , and cv.THRESH_OTSU is passed as extra flag 

thresh,thresh_img = cv.threshold(img , 0 , 255 , cv.THRESH_BINARY)

thresh = 0  the algorithm can find optimal global theshold value by drawing the image histogram , it will automically get optimal threshold value 

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
img = cv.imread("images/flower1.jpg" ,0) 
cv.imshow("Original Image" , img )


# perform Otsu threshold
# cv.threshold( src , thesh , maxVal , type) 
thresh,thresh_img = cv.threshold(img , 0 , 255 , cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow("Otsu threshold Image" , thresh_img)

img2 = cv.imread("images/otsus_algorithm.jpg",0) 
cv.imshow("Original Image 2 " , img2 )
thresh2,thresh_img2 = cv.threshold(img2 , 0 , 255 , cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow("Otsu threshold Image 2" , thresh_img2)

