
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir
https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html

http://www.tsi.enst.fr/pages/enseignement/ressources/beti/dither/arnaud/adapt.htm

Cette classe de méthodes utilise la valeur d'un seuil qui est dynamiquement changé afin de rendre compte de l'intensité locale des différentes zones de l'image d'entrée (en niveau de gris).

Les deux méthodes qui seront étudiées par la suite ( Dynamic thresholding et Constrained average thresholding ) permettent de réaliser ce seuillage adaptatif. Ces méthodes ont la particularité de rehausser le contraste ainsi que les contours, elles ont en contrepartie le désavantage de représenter les grandes surfaces de pixels à un niveau d'intensité constant.
 
 

Dynamic Thresholding

La présente méthode combine seuillage dynamique et détection de contours ce qui tend à concentrer les informations de l'image dans des zones bien spécifiques qui seront donc très détaillées. Ces zones apparaîtront dans l'image binarisée comme des zones très texturées.

Cette méthode présente de nombreuses caractéristiques :

L'image de sortie présente une résolution spatiale ainsi qu'un contraste supérieur à l'image en niveau de gris ( originale ). Le contraste de l'image originale doit être rehaussé bien qu'il y ait une perte d'information au niveau des intensités du fond de l'image.
Bien que l'entropie de l'image de sortie soit relativement faible, l'image binarisée peut être compressée par les mêmes techniques qui permettent de stocker les données, telles que le texte ou les graphiques alors que les images en niveau de gris ne peuvent pas être compressées par ces techniques ( cf. Jpeg  ).
L'algorithme du seuillage dynamique peut être implémenté en hardware à moindre coût.
Ce même algorithme peut être aussi appliqué à du texte ou à des informations graphiques avec une qualité garantie, pour les images résultantes.

 
 

Tout le problème réside dans le choix de la décision, lors de la binarisation, d'affecter la valeur 1 ou 0 aux différents pixels de l'image.
Le principe de cette méthode est le suivant :

Il s'agit de déplacer sur toute l'image un masque et de calculer en chaque pixel la valeur Dc comme indiqué sur la figure (a). Il y aura donc encore une fois des problèmes pour le traitement des bords.

Best results if an image has different lighting conditions in diffrent areas ,
Instead of suppling manually .algorithm determines the threshold for a pixel based on a few pixels surrounding it 
the function cv.adaptativeThreshold() is used which returns the thrushold image , the input arguments are :
    -1 argument is the source umage (preferably grayscale)
    -2 argument is the maximum value 
    -3 is the adaptativeMethod
    -4 argument is the simple thresholdType 
    -5 is the blockSize
    -6 argument is the constant C value 
The different type of adaptiveMethod are.
    -cv.ADAPTIVE_THRESH_NEAM_C: The mean of the surronding area minus the constant C 
    -cv.ADAPTIVE_THRESH_GAUSSIAN_C: The gaussian-weighted sum of the surrounding area minus constant C
    



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


# perform adaptive threshold
# cv.threshold( src , thesh , maxVal , type) 
thresh_img = cv.adaptiveThreshold(img , 255 ,cv.ADAPTIVE_THRESH_MEAN_C ,cv.THRESH_BINARY , 11 ,2 )
cv.imshow("Adaptive Mean C threshold Image" , thresh_img)

thresh_img = cv.adaptiveThreshold(img , 255 ,cv.ADAPTIVE_THRESH_GAUSSIAN_C ,cv.THRESH_BINARY , 11 ,2 )
cv.imshow("Adaptive Gaussian C threshold Image" , thresh_img)


img2 = cv.imread("images/plaque-voiture.jpg",0) 
cv.imshow("Original Image 2 " , img2 )

thresh_img2 = cv.adaptiveThreshold(img2 , 255 ,cv.ADAPTIVE_THRESH_MEAN_C ,cv.THRESH_BINARY , 11 ,2 )
cv.imshow("Adaptive Mean C threshold Image" , thresh_img2)

thresh_img2 = cv.adaptiveThreshold(img2 , 255 ,cv.ADAPTIVE_THRESH_GAUSSIAN_C ,cv.THRESH_BINARY , 11 ,2 )
cv.imshow("Adaptive Gaussian C threshold Image" , thresh_img2)

