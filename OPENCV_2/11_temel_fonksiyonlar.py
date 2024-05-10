import cv2

# img = cv2.imread("C:\\Users\\asus_\\PYCHARM\\OPENCV\\OPENCV_2\\test_images2\\basketbol.jpg")

# img = cv2.resize(img,(500,300))

# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)

# imgCanny = cv2.Canny(img,250,250)    # resmin hatlarını göstermeye yarar.

# cv2.imshow("blur",imgBlur)
# cv2.imshow("gray",imgGray)
# cv2.imshow("canny",imgCanny)

# cv2.waitKey(0)

#-----------------------------------------------------------------------------------------------------------------------
# image crop

img = cv2.imread("C:\\Users\\asus_\\PYCHARM\\OPENCV\\OPENCV_2\\test_images2\\basketbol.jpg")

imgCrooped = img[50:400,300:600]

cv2.imshow("original image",img)
cv2.imshow("crooped",imgCrooped)

cv2.waitKey(0)







