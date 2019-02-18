# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 18:42:54 2019

@author: AbdulBasit0044
"""
import cv2
import numpy as nm
from matplotlib import pyplot as plt

def main():
    
    #converting to Binary Image
    img = cv2.imread('C:\\Python27\\XY-cutss.PNG') #reading an image
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting to grayscale

    ret,binary_image = cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY) #converting to binary image
    cv2.imwrite('XYcutss_binary.PNG',binary_image) #saving binary image

    counter = nm.zeros(2,nm.int32)
    rows=binary_image.shape[0]
    column=binary_image.shape[1]
    print(column)

    for x in range(rows):
        if (counter[0]>(column-20))and(counter[0]<= column):
            for i in range(column):
                binary_image[x,i] = 0
            binary_image1 = cv2.imwrite("XYcutss_binary.PNG", binary_image)
        counter[0], counter[1] = 0,0
        for y in range(column):
            color = binary_image[x,y]

            if color == 255:
                counter[0] += 1
            elif color == 0:
                counter[1]+=ArithmeticError

if __name__=="__main__":
    main()
