# resimleri üst üste ekleme
import cv2
import numpy as np

img1 = cv2.imread("C:\\Users\\asus_\\PYCHARM\\OPENCV\\OPENCV_2\\test_images2\\filter.png")
img2 = cv2.imread("C:\\Users\\asus_\\PYCHARM\\OPENCV\\OPENCV_2\\test_images2\\basketbol.jpg")

img1 = cv2.resize(img1,(640,480))
img2 = cv2.resize(img2,(640,480))

toplam = cv2.addWeighted(img1,0.4,img2,0.6,0)

cv2.imshow("resim",toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()