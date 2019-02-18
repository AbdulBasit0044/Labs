# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 14:51:51 2019

@author: AbdulBasit0044
"""

from PIL import Image

def main():
    
    #opening images so that we can manipulate them and perform operations in them
    img1 = Image.open('images/B1.png').convert('LA')
    img2 = Image.open('images/B2.jpg').convert('LA')
    img3 = Image.open('images/B3.jpg').convert('LA')
    #defining global threshold vallue for all the images
    threshold = 180
    #applying threshold on all the images
    img1 = img1.point(lambda p: p > threshold and 255)
    img2 = img2.point(lambda p: p > threshold and 255)
    img3 = img3.point(lambda p: p > threshold and 255)
    #showing images in window
    img1.show("Image 1")
    img2.show("Image 2")
    img3.show("Image 3")
    #saving images in directory
    img1.save("C:\\Users\Abdul Basit\.spyder-py3\DIP Labs\Lab 03\images\Image 1")
    img2.save("C:\\Users\Abdul Basit\.spyder-py3\DIP Labs\Lab 03\images\Image 2")
    img3.save("C:\\Users\Abdul Basit\.spyder-py3\DIP Labs\Lab 03\images\Image 3")
if __name__=="__main__":
    main()
