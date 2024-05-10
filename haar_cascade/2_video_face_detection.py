import cv2

vid = cv2.VideoCapture("C:\\Users\\asus_\\PYCHARM\\OPENCV\\haar_cascade\\test_videos\\faces.mp4")

face_cascade = cv2.CascadeClassifier("C:\\Users\\asus_\\PYCHARM\\OPENCV\\haar_cascade\\datasets\\frontalface.xml")

while 1:
    _,frame = vid.read()  # başa konulan _ hata almamak için konulur.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray,1.1,2)

    for (x,y,w,h,) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)  
    cv2.imshow("image",frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

vid.release()  # videoyu daha sonra sorunsuz açmak için yazılır.
cv2.destroyAllWindows()

