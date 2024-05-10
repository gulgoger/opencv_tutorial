import cv2

img = cv2.imread("C:\\Users\\asus_\\PYCHARM\\OPENCV\\haar_cascade\\test_images\\body.jpg")

boyd_cascade = cv2.CascadeClassifier("C:\\Users\\asus_\\PYCHARM\\OPENCV\\haar_cascade\\datasets\\haarcascade_fullbody.xml") # cascade dosya ekleme

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bodies = boyd_cascade.detectMultiScale(gray,1.8,2) #detectMultiScale resmin içinde bulunan yüzlerin koordinatlarını verir

for (x,y,w,h,) in bodies:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()



