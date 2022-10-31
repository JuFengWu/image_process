import cv2
import numpy as np


img = cv2.imread("point_card.png")
hueImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


lowRange = np.array([0, 123, 100])
highRange = np.array([5, 255, 255])
# 網路上的人認為是紅色的區域

mask = cv2.inRange(hueImage, lowRange, highRange)

kernel = np.ones((3,3), np.uint8)
cv2.imshow('mask', mask)
erodedMask = cv2.erode(mask, kernel, iterations = 1)
cv2.imshow('erodedMask', erodedMask)
finalMask = cv2.dilate(erodedMask, kernel, iterations = 1)
cv2.imshow('finalMask', finalMask)

#RETR_EXTERNAL 只取最外層的輪廓
#RETR_LIST     取所有的輪廓
#CHAIN_APPROX_SIMPLE  儲存所有輪廓點
#CHAIN_APPROX_SIMPLE  每一個方向只取一的點，四邊形只有四個點
contours, hierarchy = cv2.findContours(finalMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# 獲得contours, 以及輪廓在第幾層(hierarchy, 通常不用)

for cnt in contours:
    (x,y,w,h) = cv2.boundingRect(cnt) #輪廓的四個點
    cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)
    
cv2.imshow('result', img)
while cv2.waitKey(100) != 27: #27 is esc ascii code
    if cv2.getWindowProperty("result",cv2.WND_PROP_VISIBLE)<=0:
        break
