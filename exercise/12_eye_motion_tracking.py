import cv2

vid = cv2.VideoCapture("C:\\Users\\asus_\\PYCHARM\\OPENCV\\exercise\\eye_motion.mp4")

while 1:           # tüm framleri çekmek için
    ret, frame = vid.read()    # ret,eğer framler dogru sekilde cekiliyorsa true döndürür
    if ret is False:
        break                 # false ise döngüden çık

    roi  = frame[80:210,230:450]  # region of interest 
    rows,cols,_ = roi.shape  

    gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    _,threshold = cv2.threshold(gray,3,255,cv2.THRESH_BINARY_INV)


    contours,_ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key= lambda x: cv2.contourArea(x),reverse=True)

    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)  # koordinat değerleri
        cv2.rectangle(roi,(x,y),(x+w, y+h),(255,0,0),2)
        cv2.line(roi,(x +int(w/2),0),(x+int(w/2),rows),(0,255,0),2) 
        cv2.line(roi,(0,y+int(h/2)),(cols,y + int(h/2)),(0,255,0),2) 
        break
    
    frame[80:210,230:450] = roi 
    cv2.imshow("frame",frame)

    if cv2.waitKey(80) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()

















