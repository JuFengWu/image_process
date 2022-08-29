import cv2

img = cv2.imread("../image/Lenna.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Result', img)
cv2.waitKey(0)

