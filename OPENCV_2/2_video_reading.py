import cv2

cam = cv2.VideoCapture(0)

cam.set(3,320)
cam.set(4,240)

print(cam.set(3,320))
print(cam.set(4,240))

if not cam.isOpened():          # kamera açıldı mı
    print("kamera taninmadi")
    exit()

while True:
    ret, frame = cam.read()

    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if not ret:
        print("kameradan goruntu okunamiyor")
        break

    cv2.imshow("kamera",frame)

    if cv2.waitKey(12) & 0xFF == ord("q"):
        print("goruntu sonlandirildi.")
        break

cam.release()  # kameranın arkadan çalışmaya devam etmesini tamamen durdurur.
cv2.destroyAllWindows()








