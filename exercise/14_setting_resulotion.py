import cv2

windowName = "Live Video"
cv2.namedWindow(windowName)

cap = cv2.VideoCapture(0)

print("Width: "+ str(cap.get(3)))  # cap.get(3) yazdığımızda goruntunun enini verir.4 yazarsak bıyunu verir.
print("Height: "+ str(cap.get(4)))

cap.set(3,1280)  # set ile yeniden boyutlandırıyoruz
cap.set(4,720)

print("Width*: "+ str(cap.get(3)))  
print("Height*: "+ str(cap.get(4)))

while True:
    _,frame = cap.read()
    frame = cv2.flip(frame,1)

    cv2.imshow(windowName,frame)


    if cv2.waitKey(1) == 27:     # esc ye basıldığında çık demek oluyor.
        break

cap.release()
cv2.destroyAllWindows()