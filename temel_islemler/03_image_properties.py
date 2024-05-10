
import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "test_images/opencv_logo.png"
img = cv2.imread(path)
print(img.shape)              # widht, height, channel değerlerin gösterimi
# channel : 3 ise -- color yani resim renkli
# channel : 1 ise -- grayscale yani gri tonlarda

print("width: {} pixels".format(img.shape[1]))
print("height: {} pixels".format(img.shape[0]))
print("channel: {}".format(img.shape[2]))

print("Image Size : {}".format(img.size))

print("Data Type : {}".format(img.dtype))


cv2.imshow("OPENCV",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
























