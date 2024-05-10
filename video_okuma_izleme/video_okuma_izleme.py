import cv2

cap = cv2.VideoCapture("antalya.mp4",cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if ret == 0:
        break

    frame = cv2.flip(frame,1)

    cv2.imshow("Antalya", frame)
    if cv2.waitKey(15) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()














































