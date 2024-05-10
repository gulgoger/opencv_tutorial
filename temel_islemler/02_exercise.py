import cv2

import numpy as np

import matplotlib.pyplot as plt


path = "test_images/forest.jpg"
img = cv2.imread(path)
print(img)


corner = img[0:100, 0:100]
corner_1 = img[0:100, 0:250]

img[0:100, 0:250] = (255,255,0)

cv2.imshow("Forest",img)
#cv2.imshow("Corner",corner)
#cv2.imshow("Corner-1",corner_1)

cv2.waitKey(0)
cv2.destroyAllWindows()













