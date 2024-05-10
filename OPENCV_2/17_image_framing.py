# resim cerceveleme

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\\asus_\\PYCHARM\\OPENCV\\OPENCV_2\\test_images2\\filter.png")

replicate = cv2.copyMakeBorder(img,10,10,10,10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,10,10,10,10, cv2.BORDER_REFLECT)
reflect_101 = cv2.copyMakeBorder(img,10,10,10,10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img,10,10,10,10, cv2.BORDER_WRAP)
greenColor = [0,255,0]
constant = cv2.copyMakeBorder(img,10,10,10,10, cv2.BORDER_CONSTANT, value=greenColor)   


# cv2.imshow("main",img)
# cv2.imshow("replicate",replicate)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.subplot(2,3,1), plt.imshow(img),plt.title("ORIGINAL")
plt.subplot(2,3,2), plt.imshow(replicate),plt.title("REPLICATE")
plt.subplot(2,3,3), plt.imshow(reflect),plt.title("REFLECT")
plt.subplot(234), plt.imshow(reflect_101),plt.title("REFLECT_101")
plt.subplot(235), plt.imshow(wrap),plt.title("WRAP")
plt.subplot(236), plt.imshow(constant),plt.title("CONSTANT")

plt.show()