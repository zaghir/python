# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir
"""


# import cv library
import cv2 as cv 
import numpy as np

#create a black image (canvas) of black color
#using numpy zeros method for a zeros array 
#[00000000000
# 00000000000
# 00000000000]

# 500 => with 500 => hight  3 => 3 channel
zeros_array = np.zeros((500,500,3) , dtype="uint8")
cv.imshow("Geometric Shapes " , zeros_array)

# Draw line
#specifying start , end point color and thichness
img = cv.line(zeros_array , (0,0) , (500,500) , (255,255,255) , 2)


# Draw circle
#specifying center coordinates ,radius , color and thichness
img = cv.circle(img , (250,250) , 100 , (0,255,0) , 2)
cv.imshow("Geometric Shapes " , img)

# Draw rectagle
#specifying top-left corner , bottom-tight corner points color and thichness
img = cv.rectangle(img , (50,100), ( 470,470) , (0,0,255) , 4)

# Draw Ellipse
#specifying (centerCoordinates), ()axesLength) , angle ,startAngle, endAgle, color and thichness
img = cv.ellipse(img , (200,200), ( 100,50),0,0,360,(255,0,0) , 3)

# Draw Polygon
#specifying vertices closed shape Boolean , color and thichness
#  create array of vetices with type int32 (lines joingnin clockwise direction starting  from bottom) 
#  change into an array on shape rows(-1 only one )x1x2
#  1.create a numpy array of vertices
#  2. change the shape of numpy array to -1,1,2
#  3. draw the polygon using these vertices 
vertices = np.array( [[170,400], [150,100], [250,200], [250,300]], np.int32)
vertices =vertices.reshape(-1,1,2)
img = cv.polylines(img , [vertices],True, ( 0,255,255), 5)


# Write Text 
# specifying text , (position) ,font , font size , (color)
img = cv.putText(img ,"Learn OpenCV" , (50,50) , cv.FONT_HERSHEY_SIMPLEX , 2 , (0,0,255))
     

cv.imshow("Geometric Shapes " , img)


