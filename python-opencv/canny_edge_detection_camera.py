
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir
https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html

Canny edge detection 

Detect Edges of images 

https://fr.wikipedia.org/wiki/Filtre_de_Canny
Le filtre de Canny (ou détecteur de Canny) est utilisé en traitement d'images pour la détection des contours. L'algorithme a été conçu par John Canny en 1986 pour être optimal suivant trois critères clairement explicités :

bonne détection : faible taux d'erreur dans la signalisation des contours,
bonne localisation : minimisation des distances entre les contours détectés et les contours réels,
clarté de la réponse : une seule réponse par contour et pas de faux positifs

A popular edge detection algorithm. it was developed by F.Canny 

All complixities of the multi stage algorithm is solved() by using openCV function, cv.Canny()

Apart from source image , the other two arguments are minVal and maxVal 

Intensity gradient more than maxVal are sur to be edges ans those below minVal are sure to be  non-edges 


"""


# import cv library
import cv2 as cv 


# read the image from computer
img = cv.imread("images/cat1.jpg" ) 
cv.imshow("Original Image" , img )

#canny edge detecttion code 
edges = cv.Canny(img , 110 , 210)
cv.imshow("Edge Detected Image" , edges )

cap = cv.VideoCapture(0)
while True : 
    _, frame = cap.read()
    frame = cv.cvtColor(frame , cv.COLOR_BGR2GRAY)
    blurred_frame = cv.GaussianBlur(frame , (5,5) , 0)
    
    laplacian  = cv.Laplacian(blurred_frame , cv.CV_64F)
    canny = cv.Canny(blurred_frame, 100 , 150)
    
    cv.imshow("Frame" , frame)
    cv.imshow("Laplacian" , laplacian)
    cv.imshow("Canny" , canny)
    
    key = cv.waitKey(1)