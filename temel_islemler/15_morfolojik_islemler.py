import cv2
import numpy as np

# EROZYON YÖNTEMİ

# img = cv2.imread("C:\\Users\\asus_\\PYCHARM\OPENCV\\temel_islemler\\test_images\\helikopter.jpg",0)
# kernel = np.ones((5,5),np.uint8)
# erosion = cv2.erode(img,kernel, iterations=1)

# cv2.imshow("img",img)
# cv2.imshow("erosion", erosion)

# DILATİON YÖNTEMİ

# img = cv2.imread("C:\\Users\\asus_\\PYCHARM\OPENCV\\temel_islemler\\test_images\\helikopter.jpg",0)
# kernel = np.ones((5,5),np.uint8)
# dilation = cv2.dilate(img,kernel, iterations=5)

# cv2.imshow("img",img)
# cv2.imshow("dilation", dilation)


# OPENING   --- MORPH_OPEN

# img = cv2.imread("C:\\Users\\asus_\\PYCHARM\OPENCV\\temel_islemler\\test_images\\helikopter.jpg",0)
# kernel = np.ones((5,5),np.uint8)
# opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)

# cv2.imshow("img",img)
# cv2.imshow("opening", opening)

# CLOSING  --- MORPH_CLOSE

# img = cv2.imread("C:\\Users\\asus_\\PYCHARM\OPENCV\\temel_islemler\\test_images\\helikopter.jpg",0)
# kernel = np.ones((5,5),np.uint8)
# closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

# cv2.imshow("img",img)
# cv2.imshow("closing", closing)

# GRADIENT --- MORPH_GRADIENT

# img = cv2.imread("C:\\Users\\asus_\\PYCHARM\OPENCV\\temel_islemler\\test_images\\helikopter.jpg",0)
# kernel = np.ones((5,5),np.uint8)
# gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)

# cv2.imshow("img",img)
# cv2.imshow("gradient", gradient)


# TOPHAT --- MORPH_TOPHAT

img = cv2.imread("C:\\Users\\asus_\\PYCHARM\OPENCV\\temel_islemler\\test_images\\helikopter.jpg",0)
kernel = np.ones((5,5),np.uint8)
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)

cv2.imshow("img",img)
cv2.imshow("tophat", tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()