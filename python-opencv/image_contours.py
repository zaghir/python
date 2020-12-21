
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir
https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html

Image Contours

Find and draw contours 

En traitement d'image et en vision par ordinateur, on appelle détection de contours les procédés permettant de repérer les points d'une image matricielle qui correspondent à un changement brutal de l'intensité lumineuse. Ces changements de propriétés de l'image numérique indiquent en général des éléments importants de structure dans l'objet représenté. Ces éléments incluent des discontinuités dans la profondeur, dans l'orientation d'une surface, dans les propriétés d'un matériau et dans l'éclairage d'une scène.

La détection des contours dans une image réduit de manière significative la quantité de données en conservant des informations qu'on peut juger plus pertinentes. Il existe un grand nombre de méthodes de détection des contours de l'image mais la plupart d'entre elles peuvent être regroupées en deux catégories. La première recherche les extremums de la dérivée première, en général les maximums locaux de l'intensité du gradient. La seconde recherche les annulations de la dérivée seconde, en général les annulations du laplacien ou d'une expression différentielle non linéaire.


Contours is crurve joining all the continuous points along the boundary of the image 
FindContour() function of Opencv helps in extracting the contours from the image 

Steps Involved : 
    -1 read the image from computer and make a copy of the image to display later 
    -2 Pre-rpocess the image to pass into findContours() function 
    -3 Pass pre-processed image , Contour retrieval mode and Contour approximation method into the findContours()

Will return back Detected contours and hierarchy (containing information about the image topology)

    

"""


# import cv library
import cv2 as cv 


#read the image from computer
img = cv.imread('images/plaque-voiture.jpg')
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


