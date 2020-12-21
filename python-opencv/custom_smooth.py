
"""
Created on Thu Dec 10 22:51:52 2020

@author: yzaghir

Imge Smouth (lissage)


convolution(Convoluté)
Convoluté =  Qualifie une partie d'un végétal qui est enroulé autour d'un corps ou roulé sur lui même pour former un cornet.
Exemple : Les premières petites feuilles convolutées de cette plante médicinale apparaissent au printemps.

technique : de convouté l' image 

- Done using filtring of the image using a Convolution precess where a kernel is passed over the image to generate its convoluted copy 
- Image Noise is filtred with various low-pass filters (LPF). High-pass filters (HPF)

  - LPF Removes noise from image (using bluring)
  - HPF filters help in finding edges in images  edge(bords) 

- Create a mask uning any black color shape(rectagle or circle etc)
- Averaging is a technique that takes the average of all the pixels under the kernel area and replaces the central element.
- We will use 5x5 aveagin filter kernel.

            [ 1 1 1 1 1 
     k=1/25   1 1 1 1 1 
    kernal    1 1 1 1 1 
              1 1 1 1 1 
              1 1 1 1 1 ]
            
- Open cv provides a function cv.filter2D() to convolve a kernel with an image
"""


# import cv library
import cv2 as cv 
import numpy as np

# read image from computer
img = cv.imread("images/pixelated_img.jpg") 
cv.imshow("Mascked Image" , img)


#create kernel for conolution 
custom_kernel = np.ones((5,5) , np.float32)/25

# smooth (lisse)
result = cv.filter2D(img , -1 , custom_kernel)
cv.imshow("Custom Smooth Image" , result)



