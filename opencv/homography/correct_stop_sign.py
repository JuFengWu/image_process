import cv2
import numpy as np

stopImg = cv2.imread('stop.png')

stopSignPoints = np.array([[40,19],[40,275],[271,313],[250,71]])

frontPoints = np.array([[0,0],[0,300],[300,300],[300,0]])

h, _ = cv2.findHomography(stopSignPoints,frontPoints) # 找出這四個點的homography

newImg = cv2.warpPerspective(stopImg, h, (300, 300))    # 進行透射的轉換

cv2.imshow('newImg', newImg)
cv2.waitKey(0)

