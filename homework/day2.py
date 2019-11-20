import cv2

# 以彩色圖片的方式載入
img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)

# 改變不同的 color space
img_hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_hls= cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)


while True:
    cv2.imshow('bgr', img)
    cv2.imshow('hsv', img_hsv)
    cv2.imshow('hls', img_hls)
    cv2.imshow('lab', img_lab)

    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break