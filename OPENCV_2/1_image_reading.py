import cv2
from matplotlib import pyplot as plt

resim = cv2.imread("C:\\Users\\asus_\\PYCHARM\\OPENCV\\OPENCV_2\\test_images2\\forest.jpg")

cv2.namedWindow("resim",cv2.WINDOW_NORMAL)  # window_normal penceryi büyütüp küçültebilmeye yarıyor.

cv2.imshow("resim",resim)
cv2.imshow("resim penceresi",resim)

plt.imshow(resim, cmap="gray")
plt.show()

k = cv2.waitKey(0)


if k == 27:
    print("ESC tuşuna basildi")

elif k == ord("q"):
    print("q tusuna basildi,resim kayit edildi.")
    cv2.imwrite("ormangri.jpg",resim)


#cv2.destroyWindow("resim penceresi")
cv2.destroyAllWindows()

























