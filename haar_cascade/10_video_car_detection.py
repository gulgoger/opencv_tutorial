import cv2

vid = cv2.VideoCapture("C:\\Users\\asus_\\PYCHARM\\OPENCV\\haar_cascade\\test_videos\\car.mp4")
car_cascade = cv2.CascadeClassifier("C:\\Users\\asus_\\PYCHARM\\OPENCV\\haar_cascade\\datasets\\car.xml") # cascade dosya ekleme

while 1:
    ret,frame = vid.read()
    frame = cv2.resize(frame,(640,360))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray,1.2,2) #detectMultiScale resmin içinde bulunan yüzlerin koordinatlarını verir

for (x,y,w,h,) in cars:
    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

    cv2.imshow("video",frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()