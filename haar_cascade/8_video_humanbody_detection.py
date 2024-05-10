import cv2

vid = cv2.VideoCapture("C:\\Users\\asus_\\PYCHARM\\OPENCV\\haar_cascade\\test_video\\body.mp4")
boyd_cascade = cv2.CascadeClassifier("C:\\Users\\asus_\\PYCHARM\\OPENCV\\haar_cascade\\datasets\\haarcascade_fullbody.xml") # cascade dosya ekleme


while True:
    ret,frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    bodies = boyd_cascade.detectMultiScale(gray,1.4,2) #detectMultiScale resmin içinde bulunan yüzlerin koordinatlarını verir

    for (x,y,w,h,) in bodies:
        cv2.rectangle(frame,(x,y),(y+h,x+w),(0,0,255),3)

    cv2.imshow("video",frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()



