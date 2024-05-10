import cv2
import numpy as np

img = cv2.imread("C:\\Users\\asus_\\PYCHARM\\OPENCV\\OPENCV_2\\test_images2\\sekil.jpg")
img = cv2.resize(img,(500,500))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
Canny = cv2.Canny(gray,70,150)

contours, _ = cv2.findContours(Canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 1000:
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt,True),True)   # mümküm olan en ugyun şekle yuvarlıyor
        cornerCount = len(approx)
        x,y,w,h = cv2.boundingRect(approx)
        if cornerCount == 3:
            cv2.putText(img,"Ucgen",(x+10,y+10),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0)) 
        elif cornerCount == 4:
           cv2.putText(img,"Dortgen",(x+10,y+10),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0)) 
        else:
           cv2.putText(img,"Bilinmeyen",(x+10,y+10),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0)) 

        cv2.drawContours(img,cnt,-1,(0,255,0),3)

cv2.imshow("Test",Canny)
cv2.imshow("Original",img)
cv2.waitKey(0)