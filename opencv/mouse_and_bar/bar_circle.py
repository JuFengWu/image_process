import cv2

circleSize=0
def update_it(x):
  global  circleSize 
  circleSize = x
  print(x)

img = cv2.imread("../image/Lenna.jpg")
cv2.namedWindow('image')

cv2.createTrackbar('bar','image',0,255,update_it)
center = (166,166)
color = (0,0,255)
while cv2.waitKey(100) != 27: #27 is esc ascii code
    circleImg = img.copy()
    circleImg = cv2.circle(circleImg, center, circleSize, color, -1)
    cv2.imshow("image", circleImg)
    if cv2.getWindowProperty("image",cv2.WND_PROP_VISIBLE)<=0:
        break
