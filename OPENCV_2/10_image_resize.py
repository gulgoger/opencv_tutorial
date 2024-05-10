import cv2
import numpy as np

#----------------------------------------
# RESİM BOYUTLANDIRMA (RESIZE)

# img = cv2.imread("C:\\Users\\asus_\\PYCHARM\\OPENCV\\OPENCV_2\\test_images2\\basketbol.jpg")

# print(img.shape)

# #res = cv2.resize(img,(300,300))

# res = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)

# cv2.imshow("img",img)
# cv2.imshow("res",res)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#-----------------------------------------------------
# YER DEĞİŞTİRME (TRANSLATION)

# img = cv2.imread("C:\\Users\\asus_\\PYCHARM\\OPENCV\\OPENCV_2\\test_images2\\basketbol.jpg")

# rows,cols = img.shape[:2]

# translation_matrix = np.float32([
#     [1,0,25],
#     [0,1,25]])

# img_translation = cv2.warpAffine(img,translation_matrix,(cols+50,rows+50))

# cv2.imshow("img",img)
# cv2.imshow("img_translation",img_translation)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#-----------------------------------------------------
# RESİM DÖNDÜRME (ROTATION)

# img = cv2.imread("C:\\Users\\asus_\\PYCHARM\\OPENCV\\OPENCV_2\\test_images2\\basketbol.jpg")

# rows,cols = img.shape[:2]

# rotation_matrix = cv2.getRotationMatrix2D((cols/2,rows/2),30,0.7)

# img_rotation = cv2.warpAffine(img,rotation_matrix,(int(cols*1.2),int(rows*1.2)))

# cv2.imshow("img",img)
# cv2.imshow("img_rotation",img_rotation)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


#-----------------------------------------------------
# RESİM BÜZME (AFFINE TRANSFORMATION)

# img = cv2.imread("C:\\Users\\asus_\\PYCHARM\\OPENCV\\OPENCV_2\\test_images2\\basketbol.jpg")

# rows,cols = img.shape[:2]

# src_points = np.float32([
#     [0,0],
#     [cols-1,0],
#     [0,rows-1]])

# dst_points = np.float32([
#     [0,0],
#     [int(0.6*(cols-1)),0],
#     [int(0.4*(cols-1)),rows-1]])

# affine_matrix = cv2.getAffineTransform(src_points,dst_points)

# img_output = cv2.warpAffine(img,affine_matrix,(cols,rows))

# cv2.imshow("img",img)
# cv2.imshow("img_output",img_output)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#-----------------------------------------------------
# RESİM KIRPMA (PROJECTIVE TRANSFORMATION)

# img = cv2.imread("C:\\Users\\asus_\\PYCHARM\\OPENCV\\OPENCV_2\\test_images2\\basketbol.jpg")

# rows,cols = img.shape[:2]

# src_points = np.float32([
#     [80,100],
#     [400,90],
#     [50,400],
#     [400,400]])

# dst_points = np.float32([
#     [0,0],
#     [cols-1,0],
#     [0,rows-1],
#     [cols-1,rows-1]])

# projective_matrix = cv2.getPerspectiveTransform(src_points,dst_points)

# img_output = cv2.warpPerspective(img,projective_matrix,(cols,rows))

# cv2.imshow("img",img)
# cv2.imshow("img_output",img_output)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#-----------------------------------------------------
# PAPER SCANNER UYGULAMASI YAPIMI

img = cv2.imread("C:\\Users\\asus_\\PYCHARM\\OPENCV\\OPENCV_2\\test_images2\\basketbol.jpg")

rows,cols = img.shape[:2]

click_count = 0
a = []

dst_points = np.float32([
    [0,0],
    [cols-1,0],
    [0,rows-1],
    [cols-1,rows-1]])

cv2.namedWindow("img",cv2.WINDOW_NORMAL)

def draw(event,x,y,flags,param):
    global click_count,a

    if click_count < 4:

        if event == cv2.EVENT_LBUTTONDBLCLK:
            print(click_count)
            print(x,y)
            click_count += 1
            a.append((x,y))
    else:
        src = np.float32([
            [a[0][0],a[0][1]],
            [a[1][0],a[1][1]],
            [a[2][0],a[2][1]],
            [a[3][0],a[3][1]]])
        
        click_count = 0
        a = []
        
        M = cv2.getPerspectiveTransform(src,dst_points)
        img_output = cv2.warpPerspective(img,M,(cols,rows))
        cv2.imshow("output",img_output)

    pass

cv2.setMouseCallback("img",draw)

while(1):
    cv2.imshow("img",img)
    #cv2.imshow("img_output",img_output)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()





