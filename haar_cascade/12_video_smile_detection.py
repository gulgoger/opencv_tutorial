import cv2

vid = cv2.VideoCapture("C:\\Users\\asus_\\PYCHARM\\OPENCV\\haar_cascade\\test_images\\smile.mp4")

face_cascade = cv2.CascadeClassifier("C:\\Users\\asus_\\PYCHARM\\OPENCV\\haar_cascade\\datasets\\frontalface.xml") # cascade dosya ekleme
smile_cascade = cv2.CascadeClassifier("C:\\Users\\asus_\\PYCHARM\\OPENCV\\haar_cascade\\datasets\\smile.xml")


while True:
    ret,frame = vid.read()
    frame = cv2.resize(frame,(640,480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,5) #detectMultiScale resmin içinde bulunan yüzlerin koordinatlarını verir
    
    for (x,y,w,h,) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)


    roi_img = frame[y:y+h, x:x+w]
    roi_gray = gray[y:y+h, x:x+w]

    
    smiles = smile_cascade.detectMultiScale(roi_gray,1.3,5)

    for (sx,sy,sw,sh) in smiles:
        cv2.rectangle(roi_img,(sx,sy),(sx+sw,sy+sh),(0,255,0),2)

    cv2.imshow("img",frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()


