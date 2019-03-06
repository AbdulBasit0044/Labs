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
    gray_img = cv2.imread('C:\\Users\Abdul Basit\.spyder-py3\DIP Labs\Lab 03-Abdul Basit\images\XY-cutss.png',0) #reading an image
    #gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting to grayscale
    print("1")
    ret,binary_image = cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY) #converting to binary image
    cv2.imwrite('images\XYcutss_binary.PNG',binary_image) #saving binary image
    print("2")
    counter = nm.zeros(2,nm.int32)
    print("4")
    print (gray_img)
    rows=binary_image.shape[0]
    print("3")
    column=binary_image.shape[1]
    print(column)
    print("Columns are printed")
    for x in range(rows):
        print("Columns are printed")
        if (counter[0]>(column-20))and(counter[0]<= column):
            for i in range(column):
                binary_image[x,i] = 0
                print("Columns are printed")
            binary_image1 = cv2.imwrite("images\XYcutss_binary.PNG", binary_image)
        counter[0], counter[1] = 0,0
        for y in range(column):
            color = binary_image[x,y]

            if color == 255:
                counter[0] += 1
            elif color == 0:
                counter[1]=counter[1]+0
if __name__=="__main__":
    main()
