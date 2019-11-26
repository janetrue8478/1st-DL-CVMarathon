import cv2
import numpy as np
img=cv2.imread('lena.jpg',cv2.IMREAD_COLOR)

#1.改變飽和度
#轉換成HSV格式
img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
change_percentage=0.2

img_hsv_down=img_hsv.astype('float32')
img_hsv_down[:,:,-1]= img_hsv_down[:,:,-1]/255-change_percentage
img_hsv_down[img_hsv_down[:,:,-1]<0]=0
img_hsv_down[:,:,-1]=img_hsv_down[:,:,-1]*255
img_hsv_down=img_hsv_down.astype('uint8')

img_hsv_up=img_hsv.astype('float32')
img_hsv_up[:,:,-1]= img_hsv_up[:,:,-1]/255+change_percentage
img_hsv_up[img_hsv_down[:,:,-1]<0]=0
img_hsv_up[:,:,-1]=img_hsv_up[:,:,-1]*255
img_hsv_up=img_hsv_up.astype('uint8')

img_hsv_down=cv2.cvtColor(img_hsv_down,cv2.COLOR_HSV2BGR)
img_hsv_up=cv2.cvtColor(img_hsv_up,cv2.COLOR_HSV2BGR)

img_hsv_change=np.hstack((img,img_hsv_down,img_hsv_up))
while True:
    cv2.imshow('change saturation',img_hsv_change)
    
    k=cv2.waitKey(0)
    if k==27:
        cv2.destroyAllWindows()
        break
#2.實作直方圖均衡
#case1:把彩圖拆開對每個 channel 個別做直方圖均衡再組合起來
#以紅色顯示
img_r=img[:,:,2]
img_r_hist=cv2.equalizeHist(img_r)
#以綠色顯示
img_g=img[:,:,1]
img_g_hist=cv2.equalizeHist(img_g)
#以藍色顯示
img_b=img[:,:,0]
img_b_hist=cv2.equalizeHist(img_b)
img_bgr_equal =img_r_hist+img_g_hist+img_b_hist


#case2: 轉換 color space 到 HSV 之後對其中一個 channel 做直方圖均衡
img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_s=img[:,:,2]
img_hsv_equal=cv2.equalizeHist(img_s)

img_bgr_equalHist = np.hstack((img, img_bgr_equal, img_hsv_equal))
while True:
    cv2.imshow('img_s_equal',img_bgr_equalHist)
    
    k=cv2.waitKey(0)
    if k==27:
        cv2.destroyAllWindows()
        break

#3.alpha/ beta 調整對比 / 明亮
# alpha: 控制對比度 (1.0~3.0)
# beta: 控制明亮度 (0~255)
add_contrast = cv2.convertScaleAbs(img,alpha=2.0,beta=0)
add_lighness = cv2.convertScaleAbs(img,alpha=1.0,beta=200)
img_contrast_light=np.hstack((add_contrast,add_lighness))
while True:
    cv2.imshow('img_contrast_light',img_contrast_light)
    k=cv2.waitKey(0)
    
    if k==27:
        cv2.destroyAllWindows()
        break
