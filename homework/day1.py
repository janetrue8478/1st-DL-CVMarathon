import cv2

# 以彩色圖片的方式載入
img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)

#以紅色顯示
img_r=img.copy()
img_r[:,:,0]=0
img_r[:,:,1]=0

#以綠色顯示
img_g=img.copy()
img_g[:,:,0]=0
img_g[:,:,2]=0


#以藍色顯示
img_b=img.copy()
img_b[:,:,1]=0
img_b[:,:,2]=0

while True:
    cv2.imshow('R-RGB', img_r)
    cv2.imshow('G-RGB', img_g)
    cv2.imshow('B-RGB', img_b)

    k = cv2.waitKey(0)
    if k == 27:       
        cv2.destroyAllWindows()
        break
