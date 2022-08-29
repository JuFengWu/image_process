import cv2

img = cv2.imread('stop.png')

img = cv2.circle(img, (40,19), 5, (0,0,255), -1)
img = cv2.circle(img, (40,275), 5, (0,0,255), -1)
img = cv2.circle(img, (271,313), 5, (0,0,255), -1) 
img = cv2.circle(img, (250,71), 5, (0,0,255), -1) # book png four points
cv2.imshow('image',img)
cv2.waitKey(0)