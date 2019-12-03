import cv2
import numpy as np
img=cv2.imread('lena.jpg',cv2.IMREAD_COLOR) 
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#比較 Sobel 如果在 uint8 的情況下做會 overflow 的狀況
img_sobel_x=cv2.Sobel(img_gray,cv2.CV_16S,dx=1,dy=0,ksize=3)
img_sobel_x=cv2.convertScaleAbs(img_sobel_x)

img_sobel_x_uint8 =cv2.Sobel(img_gray,-1,dx=1,dy=0,ksize=3)
img_sobel_x_uint8=cv2.convertScaleAbs(img_sobel_x_uint8)

img_show=np.hstack((img_gray,img_sobel_x, img_sobel_x_uint8))
while True:
    cv2.imshow('Edge Detection', img_show)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break
#比較一次與兩次計算偏微分的結果
# 求二次導數取得邊緣檢測結果
img_sobel_xx = cv2.Sobel(img_gray,cv2.CV_16S,dx=2,dy=0,ksize=3)
img_sobel_xx=cv2.convertScaleAbs(img_sobel_xx)

img_show = np.hstack((img_gray, img_sobel_x, img_sobel_xx))
while True:
    cv2.imshow('Edge Detection', img_show)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break
