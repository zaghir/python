# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir

Morphology Transormation 

Morphology mean study of form and structure.
Any Chnages in form and strcuture is transformation

We need two inputs to perform morphological transformation 
- one is our original image
- sencond one is structuring element or kernel which decides the natural of operation

Morphology Transormation -Erosion
- it erodes away the boundaries of the object is focus(foreground)
- All th pixel near boundary will be discarder depending upon the size of kernel 
- Useful for removing small white noises images
# create a numpy array 
# A 5x5 kernal with full of ones 
  trans_kernal = np.ones(5,5), np.uint8)
  trans_image = cv.erode(img.kernel.iterations = 1)
  
  
Morphology Transormation - Dilation 
- The opposite of erosion happens in dilation.
- increases the white region in the image 
- typically in cases like black noise removal. erosion is followed dilation 
- Since erosion removes white noise but is alse shrinks object. So we dilate it 

"""


# import cv library
import cv2 as cv 
import numpy as np

# read image from computer
img = cv.imread("images/dog1.jpg") 

# show the Actual Image
cv.imshow("original" , img)

# create an ones array of size 5x5 
trans_kernal = np.ones((5,5), dtype="uint8")

#defining the erosion transformation 
trans_image = cv.erode(img ,trans_kernal ,iterations= 1)

# show the erosion Transformation 
cv.imshow("Erode Transformation" , trans_image)


#defining the dilation transformation 
trans_image = cv.dilate(img ,trans_kernal ,iterations= 1)

# show the dilation Transformation 
cv.imshow("Dilate Transformation" , trans_image)


"""
Morphology Transormation - Opening 
it s actually erosion followed by dilation
used for white noise removal
using the function cv.morphologyEx() with morphology operation enum

"""
# define the opening transformation 
trans_image= cv.morphologyEx(img , cv.MORPH_OPEN, trans_kernal)

# show the opening Transformation 
cv.imshow("Opening Transformation" , trans_image)


"""
Morphology Transormation - Closing
it s actually dilation followed by erosion 
used for small block noise removal
"""
# define the closing transformation 
trans_image= cv.morphologyEx(img , cv.MORPH_CLOSE, trans_kernal)

# show the closing Transformation 
cv.imshow("Closing Transformation" , trans_image)


"""
Morphology Transormation - Gradient
it s actually diffrence between dilation and erosion 
resulat will give an outline of the image 
"""
# define the gradient transformation 
trans_image= cv.morphologyEx(img , cv.MORPH_GRADIENT, trans_kernal)

# show the closing Transformation 
cv.imshow("Gradient Transformation" , trans_image)


"""
Morphology Transormation - Top Hat
it s actually diffrence between input image and Opering  of the imafe
resulat will get rid of overlapping parts of image
"""
# define the gradient transformation 
trans_image= cv.morphologyEx(img , cv.MORPH_TOPHAT, trans_kernal)

# show the Top Hat Transformation 
cv.imshow("Top Hat Transformation" , trans_image)


"""
Morphology Transormation - Blak Hat
it s actually diffrence between input image and Closing  of the imafe
resulat will get rid of all parts than the overlapping parts of image
"""
# define the Black hat transformation 
trans_image= cv.morphologyEx(img , cv.MORPH_BLACKHAT, trans_kernal)

# show the Black Hat Transformation 
cv.imshow("Black Hat Transformation" , trans_image)
