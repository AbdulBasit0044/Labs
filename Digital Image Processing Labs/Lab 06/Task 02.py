# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 21:39:35 2019

@author: AbdulBasit0044
"""

from PIL import Image
from PIL import ImageOps
import cv2
import numpy as np
from matplotlib import pyplot as plt

 
def main():
    #OPENING IMAGE
    img = Image.open("image.jpg")
    #CREATING NUMPY ARRAY
    imageArray = np.array(img)
    #CALCULATING HISTOGRAM USING OPENCV
    histogram = cv2.calcHist([imageArray],[0],None,[256],[0,256])
    plt.hist(imageArray.ravel(),256,[0,256])
    #PLOTTING IT ON X-Y XIS
    plt.show()
    #EQUALIZING IMAGE
    equalizedImage = ImageOps.equalize(img)
    #CREATING ARRAY OF EQUALIZED IMAGE
    imageArray1 = np.array(equalizedImage)
    histogram = cv2.calcHist([imageArray1],[0],None,[256],[0,256])
    #PLOTTING HISTOGRAM
    plt.hist(imageArray1.ravel(),256,[0,256])
    #SHOWING IMAGE ON PLOT
    plt.show()
    #SHOWING IMAGE IN WINDOW
    equalizedImage.show()
    #SAVING IMAGE
    equalizedImage.save('image.jpg')

#CALLING IF MAIN FUNCTION EXISTS    
if __name__=="__main__":
    main()