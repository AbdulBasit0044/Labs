from PIL import Image
import numpy as nm
from matplotlib import pyplot as plt

 
def main():
    
    #OPENING IMAGE IN GRAY SCALE
    img = Image.open("image.jpg").convert("L")
    #CREATING NUMPY ARRAY
    imageArray = nm.array(img)
    
    #EXTRACTING PARAMETERS
    rows = len(imageArray)
    colomns = len(imageArray[0])
    #NUMPY ARRAY
    imageArray1 = nm.zeros(imageArray.shape, dtype = int)
    
    #NESTED LOOPS TO APPLY POWER LOG METHOD
    for x in range(rows):
        for y in range(colomns):
            #ENHANCING IMAGE
            imageArray1[x][y] = pow(imageArray[x][y],1.05)
    #SHOWING IMAGE IN WINDOW
    Image.fromarray(imageArray1).show()

#CALLING IF MAIN FUNCTION EXISTS    
if __name__=="__main__":
    main()