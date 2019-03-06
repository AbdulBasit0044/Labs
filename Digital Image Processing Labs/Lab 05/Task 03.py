# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 02:39:22 2019

@author: AbdulBasit0044
"""

import cv2
import numpy as np
from matplotlib import image as imag

def main():
    
    img=cv2.imread('images\\dollar.tif',0)
    
    
    height=img.shape[0]
    width=img.shape[1]
    
    print(height)
    print(width)
    L=256
    plane=1
    for j in range(0,8):
        for x in range(0,500):
            for y in range(0,height):
                if((img[x,y] & plane) == 0):
                    img[x,y]=0
                else:
                    img[x,y]=255
                    
        plane*=2
        cv2.imwrite("images\Result_of_Task_01_plane_"+str(j+1)+".jpg",img)
    #cv2.imshow("Result",img)
    #if cv2.waitKey(1)==27:
    #    cv2.destroyWindow(Result)
    
if __name__=="__main__":
    main()