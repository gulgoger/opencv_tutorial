import cv2

img = cv2.imread("klon.jpg")  # resim çağırma yani kullanacağımız resim
# print(img)

cv2.namedWindow("image",cv2.WINDOW_NORMAL)   # resim için bir pencere açmamızı sağlar. cv2.WINDOW_NORMAL resmi büytüp küçültebilmemize yarar.

cv2.imshow("image",img)  # resim penceresinin adı
cv2.imwrite("klon1.jpg",img)
cv2.waitKey(0)            # herhangi bir tuşa basana kadar resmin ekranda kalması için
cv2.destroyAllWindows()  # olması gereken bir kod iskelet.
































