# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 17:44:11 2019

@author: AbdulBasit0044
"""
import cv2
import numpy as nm
from matplotlib import pyplot as plt

def main():
    
    #converting to Binary Image
    img = cv2.imread('images/B3.png') #reading an image
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting to grayscale

    bins = nm.zeros(256, nm.int32) #creating bins

    flatten = nm.ravel(gray_img, nm.int32) #flattening image

    for x in flatten: 
        bins[x]+=1  #storing flatten image in bins

    bins = bins/3

    dic ={} #dictionary datastructure

    for key,value in enumerate(bins): 
        dic[key]=value #storing values against key

    plt.bar(dic.keys(),dic.values()) #plotting keys against values
    plt.show() #showing plotted histogram

if __name__=="__main__":
    main()
