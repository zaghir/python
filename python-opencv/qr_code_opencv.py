
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir



"""


# import cv library
import cv2 as cv 
#import numpy as np
from pyzbar.pyzbar import decode

#img = cv.imread('images/qrcode.png')

#code = decode(img)
#print(code)
#for barcode in decode(img):
#    print(barcode.rect)
#    print(barcode.data)
#    myData = barcode.data.decode('utf-8')
#    print(myData)
    
cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success , img = cap.read()    
    print(decode(img))
    for barcode in decode(img):        
        print(barcode.data)        
        myData = barcode.data.decode('utf-8')
        print(myData)
        # create poligon
        #pts = np.array([barcode.polygon] , np.int32)
        #pts = pts.reshape((-1,1,2))
        #cv.polylines(img, [pts],True,(255,0,255),5)
        #pts2 =barcode.rect
        #cv.putText(img, myData, (pts2[0],pts2[1]),cv.FONT_HERSHEY_SIMPLEX ,0.9 ,(255,0,255),2)
        
    cv.imshow('Result' , img)
    cv.waitKey(1)
    

"""

"""