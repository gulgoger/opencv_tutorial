import cv2

img = cv2.imread("C:\\Users\\asus_\\PYCHARM\\OPENCV\\haar_cascade\\test_images\\car.jpg")

car_cascade = cv2.CascadeClassifier("C:\\Users\\asus_\\PYCHARM\\OPENCV\\haar_cascade\\datasets\\car.xml") # cascade dosya ekleme

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cars = car_cascade.detectMultiScale(gray,1.1,1) #detectMultiScale resmin içinde bulunan yüzlerin koordinatlarını verir

for (x,y,w,h,) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()