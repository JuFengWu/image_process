import cv2

img = cv2.imread("Lenna.jpg")

x = 100
y = 100

# 裁切區域的長度與寬度
w = 250
h = 150

# 裁切圖片
crop_img = img[y:y+h, x:x+w]
cv2.imshow("crop img",crop_img)
cv2.waitKey(0)