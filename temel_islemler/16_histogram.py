import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\\asus_\\PYCHARM\OPENCV\\temel_islemler\\test_images\\helikopter.jpg")
b,g,r = cv2.split(img)
cv2.imshow("img",img)


plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
