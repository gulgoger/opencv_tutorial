
import cv2
import numpy as np

path ="test_images/opencv_logo.png"
img = cv2.imread(path)
#print(img)

#px = img[10,10]
#print(px)

(b,g,r) = img[50,30]
print("(0,0) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

print("RED Value (before): ",img.item(10,10,2))

img.itemset((10,10,2),100)
print("RED Value (after): ",img.item(10,10,2))















