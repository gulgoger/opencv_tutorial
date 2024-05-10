import cv2

img = cv2.imread("C:\\Users\\asus_\\PYCHARM\\OPENCV\\haar_cascade\\test_images\\smile.jpg")
face_cascade = cv2.CascadeClassifier("C:\\Users\\asus_\\PYCHARM\\OPENCV\\haar_cascade\\datasets\\frontalface.xml") # cascade dosya ekleme
smile_cascade = cv2.CascadeClassifier("C:\\Users\\asus_\\PYCHARM\\OPENCV\\haar_cascade\\datasets\\smile.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.3,7) #detectMultiScale resmin içinde bulunan yüzlerin koordinatlarını verir

for (x,y,w,h,) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)


roi_img = img[y:y+h, x:x+w]
roi_gray = gray[y:y+h, x:x+w]

smiles = smile_cascade.detectMultiScale(roi_gray,1.3,5)

for (sx,sy,sw,sh) in smiles:
    cv2.rectangle(roi_img,(sx,sy),(sx+sw,sy+sh),(0,255,0),2)


cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


