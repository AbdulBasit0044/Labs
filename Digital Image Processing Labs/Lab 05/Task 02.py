# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 02:13:16 2019

@author: AbdulBasit0044
"""

import cv2
import numpy as np

def main():
    
    img1=cv2.imread("images\\lena_color_256.tif")
    img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    #ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    #print(thresh1)
    #img=thresh1
    #print(img)
    height=img.shape[0]
    width=img.shape[1]
    print(height)
    print(width)
    for x in range(0,width-1):
        for y in range(0,height):
            img[x,y]=abs(img[x+1,y]-img[x,y])
    cv2.imwrite("images\Result_of_Task_02.jpg",img)
    
if __name__=="__main__":
    main()