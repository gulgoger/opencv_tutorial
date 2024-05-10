import cv2
import numpy as np


img = np.zeros((512,512,3),np.uint8)

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2)
cv2.rectangle(img,(125,125),(250,250),(0,0,255),-1)
cv2.circle(img,(256,256),100,(255,0,0),-1)
cv2.ellipse(img,(256,256),(125,50),15,0,360,(0,255,0),-1)

cv2.imshow("Photo",img)
cv2.waitKey(0)














