import cv2

vid = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("C:\\Users\\asus_\\PYCHARM\\OPENCV\\haar_cascade\\datasets\\frontalface.xml")

while 1:
    ret,frame = vid.read()  # başa konulan _ hata almamak için konulur. alt tire yerine ret de yazılır
    frame = frame.flip(frame,1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray,1.6,5)

    for (x,y,w,h,) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)  

    cv2.imshow("video",frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

vid.release()  # videoyu daha sonra sorunsuz açmak için yazılır.
cv2.destroyAllWindows()

