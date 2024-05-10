import cv2
import numpy as np

image_path = "C:\\Users\\asus_\\PYCHARM\\OPENCV\\exercise\\starwars.jpg"
template_path = "C:\\Users\\asus_\\PYCHARM\\OPENCV\\exercise\\starwars2.jpg"

img = cv2.imread(image_path)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

template = cv2.imread(template_path,cv2.IMREAD_GRAYSCALE)
w,h = template.shape[::-1]

result = cv2.matchTemplate(gray_img,template,cv2.TM_CCOEFF_NORMED) # matchtemplate şablonu resimde aynı yere konumlandırır.
location = np.where(result >= 0.95)

for point in zip(*location[::1]):
    cv2.rectangle(img,point,(point[0]+w,point[1]+h),(0,255,0),3)



cv2.imshow("image",img)
cv2.waitKey()
cv2.destroyAllWindows()