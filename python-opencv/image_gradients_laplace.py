
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir
https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html

Canny edge detection 

Detect Edges of images 

An image gradient is a directional change in the intensity or color in an image. The gradient of the image is one of the fundamental building blocks in image processing. For example, the Canny edge detector uses image gradient for edge detection. In graphics software for digital image editing, the term gradient or color gradient is also used for a gradual blend of color which can be considered as an even gradation from low to high values, as used from white to black in the images to the right. Another name for this is color progression.

Mathematically, the gradient of a two-variable function (here the image intensity function) at each image point is a 2D vector with the components given by the derivatives in the horizontal and vertical directions. At each image point, the gradient vector points in the direction of largest possible intensity increase, and the length of the gradient vector corresponds to the rate of change in that direction.[1]

Since the intensity function of a digital image is only known at discrete points, derivatives of this function cannot be defined unless we assume that there is an underlying continuous intensity function which has been sampled at the image points. With some additional assumptions, the derivative of the continuous intensity function can be computed as a function on the sampled intensity function, i.e., the digital image. Approximations of these derivative functions can be defined at varying degrees of accuracy. The most common way to approximate the image gradient is to convolve an image with a kernel, such as the Sobel operator or Prewitt operator.



An image gradient can be difined as the directional change in the intensity or color int that image 
It can be considered as one of the fundamental building blocks in image processiong 

For instance ,the canny edge detector we just learned , uses image gradient for edge detection .

The popilare gradient functions included in OpenCv are cv.Sobel , cvLapacian()

Sobel is a Gaussian smoothing with differentiantion operation, more resistant to noise 
The lapacian derivative of the image given by the relation  

"""


# import cv library
import cv2 as cv 


# read the image from computer
img = cv.imread("images/cat1.jpg" ) 
cv.imshow("Original Image" , img )

#Laplacian gradient 
gradient = cv.Laplacian(img , cv.CV_64F)
cv.imshow("Laplacian Gradient" , gradient )

#Sobel x gradient 
gradient = cv.Sobel(img , cv.CV_64F , 1,0 , ksize= 5 )
cv.imshow("Sobel x Gradient" , gradient )

#Sobel y gradient 
gradient = cv.Sobel(img , cv.CV_64F , 0,1 , ksize= 5 )
cv.imshow("Sobel y Gradient" , gradient )
