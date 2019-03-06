# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:20:22 2019

@author: AbdulBasit0044
"""

import cv2
import numpy as np
from matplotlib import image as imag

def main():
    
    img=cv2.imread('images\\lena_color_256.tif')
    
    
    height=img.shape[0]
    width=img.shape[1]
    
    #print(height)
    #print(width)
    L=256
    for x in range(0,width):
        for y in range(0,height):
            element_length=img[x,y].shape[0]
            #print(element_length)
            if(element_length==1):
                img[x,y]=abs(L-1-img[x,y])
            elif(element_length==3):
                img[x,y]=[abs(L-1-img[x,y,0]),abs(L-1-img[x,y,1]),abs(L-1-img[x,y,2])]
                
    cv2.imwrite("images\Result_of_Task_01.jpg",img)
    #cv2.imshow("Result",img)
    #if cv2.waitKey(1)==27:
    #    cv2.destroyWindow(Result)
    
if __name__=="__main__":
    main()