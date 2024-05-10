import cv2
import matplotlib.pyplot as plt

resim = cv2.imread("C:\\Users\\asus_\\PYCHARM\\OPENCV\\OPENCV_2\\test_images2\\forest.jpg")

kirp = resim[200:300,100:250]

resim[100:200,200:350] = kirp

plt.subplot(121)
plt.imshow(resim)
plt.subplot(122)
plt.imshow(kirp)
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()