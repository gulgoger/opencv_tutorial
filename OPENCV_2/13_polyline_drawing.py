import cv2
import numpy as np


img = np.zeros((512,512,3),np.uint8)

pts = [(55,55),(243,344),(22,143),(54,500)]

cv2.polylines(img,np.array([pts]),True,(255,0,0),3)

cv2.putText(img,"OPENCV DERSLERI",(35,35),cv2.FONT_HERSHEY_COMPLEX,0.9,(230,42,44),1)

cv2.imshow("Photo",img)
cv2.waitKey(0)
