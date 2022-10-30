import cv2

img = cv2.imread("../image/Lenna.jpg")

center = (166,166)
radius  =10
color = (0,0,255)
thinkness = 3 #pix
circleImg = cv2.circle(img,center,radius,color, thinkness)
center = (208,166)
circleImg = cv2.circle(img,center,radius,color, -1)

cv2.imshow("image",img)
cv2.waitKey(0)