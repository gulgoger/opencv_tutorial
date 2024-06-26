import cv2
import numpy as np

img = np.zeros((512,512,3),dtype = np.uint8)

# line draw
# cv2.line(img,(0,0),(511,511),(255,0,0),thickness=5)
# cv2.line(img,(50,400),(400,50),(0,255,0),thickness=10)

# rectangle draw
# cv2.rectangle(img,(50,50),(300,300),(0,0,255),5)
# cv2.rectangle(img,(300,300),(511,511),(0,0,255),-1)

# circle draw
# cv2.circle(img,(255,255),60,(120,40,200),2)
# cv2.circle(img,(100,100),90,(255,50,230),-1)

# ellipse draw
# cv2.ellipse(img,(256,256),(100,50),0,0,180,(255,100,0),3)
# cv2.ellipse(img,(100,100),(100,50),0,0,180,(255,100,0),-1)

# polyline draw
# pts = np.array([[20,30],[100,120],[255,255],[10,400]],np.int32)
# pts2 = pts.reshape(-1,1,2)

# cv2.polylines(img,[pts],True,(255,255,255),3)

# text
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,"OPENCV",(10,400),font,4,(0,155,255),2,cv2.LINE_AA)


cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
















