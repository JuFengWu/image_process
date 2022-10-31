import cv2
import numpy as np


img = cv2.imread("point_card.png")
hueImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


lowRange = np.array([10, 43, 46])
highRange = np.array([40, 255, 255])

mask = cv2.inRange(hueImage, lowRange, highRange)
cv2.imshow('mask', mask)
res = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('Input', img)
cv2.imshow('Result', res)
while cv2.waitKey(100) != 27: #27 is esc ascii code
    if cv2.getWindowProperty("Input",cv2.WND_PROP_VISIBLE)<=0:
        break

