
import cv2
import numpy as np

import matplotlib.pyplot as plt

path = "test_images/opencv_logo.png"
img = cv2.imread(path) 
print("Shape: {}".format(img.shape))


(B,G,R) = cv2.split(img)
merged = cv2.merge([B,G,R])

black = np.zeros(img.shape[:2], dtype="uint8")


cv2.imshow("Red",cv2.merge([black,black,R]))
cv2.imshow("Green",cv2.merge([black,G,black]))
cv2.imshow("Blue",cv2.merge([B,black,black]))

# cv2.imshow("OPENCV-merged",merge)
# cv2.imshow("OPENCV-B",B)
# cv2.imshow("OPENCV-G",G)
# cv2.imshow("OPENCV-R",R)

cv2.waitKey(0)
cv2.destroyAllWindows()
