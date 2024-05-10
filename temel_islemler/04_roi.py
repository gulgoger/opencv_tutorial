# ROI: REGION OF INTEREST

import cv2
import numpy as np

import matplotlib.pyplot as plt

path = "test_images/basketbol.jpg"
img = cv2.imread(path) 
print("Shape: {}".format(img.shape))

roi = img[100:200, 0:50]
img[300:400, 300:350] = roi

cv2.imshow("Basketbol",img)
cv2.imshow("Basketbol ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()






