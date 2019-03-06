# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:29:06 2019

This is Lab 04 to detect the objects in a image

@author: AbdulBasit0044
"""
#importting libraries for the image manipulation
import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as img

#defining main function
def main():
    
    
    
    #READING IMAGE IN GRAY SCALE FORMAT
    gray_img = cv2.imread('Lab4-image.PNG',0)
    #CONVERTING IMAGE TO BINARY
    ret,thresh1 = cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)
    #SAVING BINARY IMAGE TO THE DISK
    binary_img = cv2.imwrite('Lab4-binary-image.jpg',thresh1)
    #EXTRACTING PARAMETERS FROM IMAGE
    height = thresh1.shape[0]
    width = thresh1.shape[1]
    #READING IMAGE
    image = img.imread('Lab4-binary-image.jpg')
    
    #INITIALIZING NUMPY ARRAY FOR THE DARK BACKGROUND
    empty = np.zeros((height,width),np.int32)
    
    count = 20
    #INITIALIZING DICTIONARY
    dic = {}
    #NESTED LOOPS FOR THE CONNECTED COMPONENT LABELLING ALGORITHM
    for x in range(height):
        for y in range(width):
            color = thresh1[x,y]
            if color == 0:
                left = empty[x,y-1]
                top = empty[x-1,y]
                if left > 0 and top > 0:
                    empty[x,y] = min(left,top)
                    if left != top:
                        dic.update([(max(left,top),min(left,top))])
                elif left > 0:
                    empty[x,y] = left
                elif top > 0:
                    empty[x,y] = top
                else:
                    count = count+20
                    empty[x,y] = count
    #ADDING (KEY,VALUE) PAIRS TO THE DICTIONARY
    key = list(dic.keys())
    val = list(dic.values())
    #GIVING COLORS TO THE DICTIONARY CO-ORDINATES
    for x in range(height):
        for y in range(width):
            colors = empty[x,y]
            for z in range(len(key)):
                if colors == key[z]:
                    empty[x,y] = val[z]
    #SHOWING IMAGE WITH THE COLORED VALUE IN THE CONSOLE
    plt.imshow(empty,cmap="nipy_spectral")
    plt.show()
    plt.savefig('Final-image.jpg')
    
#CALLING MAIN IF ANY MAIN METHOD EXISTS IN THE PROGRAM    
if __name__=="__main__":
    main()