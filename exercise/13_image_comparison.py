import cv2
import numpy as np

path1 = "C:\\Users\\asus_\\PYCHARM\\OPENCV\\exercise\\aircraft.jpg"
path2 = "C:\\Users\\asus_\\PYCHARM\\OPENCV\\exercise\\aircraft1.jpg"

img1 = cv2.imread(path1)
img1 = cv2.resize(img1,(640,550))

img2 = cv2.imread(path2)
img2 = cv2.resize(img2,(640,550))

img3 = cv2.medianBlur(img1,7)

"""
if img1.shape == img2.shape:
    print("same size")
else:
    print("not same")
"""

diff = cv2.subtract(img1,img3)   # 2 resmi karşılaştırıp farklı olan yerlerin rengini değiştirir.
b,g,r = cv2.split(diff)

if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r)== 0: #değişkeni tek tek tarar kaç tane sıfır olmadığına bakar
    print("completely equal")
else:
    print("NOT completely equal")

cv2.imshow("Difference",diff)

cv2.waitKey(0)
cv2.destroyAllWindows()


