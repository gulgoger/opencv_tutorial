import cv2

img = cv2.imread("C:\\Users\\asus_\\PYCHARM\\OPENCV\\exercise\\starwars.jpg")
blurry_img = cv2.medianBlur(img,7)

laplacian = cv2.Laplacian(blurry_img,cv2.CV_64F).var()  # laplacian bulanıklık değerini verir

if laplacian < 500:
    print("blurry image")

cv2.imshow("img",img)
cv2.imshow("blurry_image",blurry_img)
cv2.waitKey()
cv2.destroyAllWindows()