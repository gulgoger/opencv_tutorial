import cv2
import numpy as np


img = np.zeros((512,512,3),np.uint8)

def changeThickness(x):
    img = np.zeros((512,512,3),np.uint8)
    cv2.line(img,(0,0),(512,512),(255,0,0),x)
    cv2.imshow("Photo",img)

cv2.imshow("Photo",img)
cv2.createTrackbar("Thickness","Photo",1,15,changeThickness)

cv2.waitKey(0)
