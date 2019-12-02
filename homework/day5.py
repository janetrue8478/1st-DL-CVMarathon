import cv2
import numpy as np
img=cv2.imread('lena.jpg',cv2.IMREAD_COLOR)

point1=(60, 40)
point2=(420, 510)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_hsv[...,-1]=cv2.equalizeHist(img_hsv[...,-1])
img_equal=cv2.cvtColor(img_hsv,cv2.COLOR_HSV2BGR)

#矩形

cv2.rectangle(img_equal,point1,point2,(0,0,255),3)

img_equal=img_equal[:,::-1,:]
img_resize=cv2.resize(img_equal,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)


while True:
    cv2.imshow('image',img_resize)
    k=cv2.waitKey(0)
    if k==27:
        cv2.destroyAllWindows()
        break