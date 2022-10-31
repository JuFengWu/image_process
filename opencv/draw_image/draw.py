import cv2

img = cv2.imread("../image/Lenna.jpg")

cv2.imshow("image", img)

while cv2.waitKey(100) != 27: #27 is esc ascii code
    if cv2.getWindowProperty("image",cv2.WND_PROP_VISIBLE)<=0:
        break

center = (166,166)
radius = 10
color = (0,0,255)
thickness = 3 #px
circleImg = cv2.circle(img, center, radius, color, thickness)
center = (208,166)
circleImg = cv2.circle(img, center, radius, color, -1)

cv2.imshow("image", circleImg)
while cv2.waitKey(100) != 27: #27 is esc ascii code
    if cv2.getWindowProperty("image",cv2.WND_PROP_VISIBLE)<=0:
        break
        
point1 = (166,166)
point2 = (20,50)
color = (255,0,0)
thickness = 1 #px
rectangleImg = cv2.rectangle(img, point1, point2, color, thickness)

cv2.imshow("image", rectangleImg)
while cv2.waitKey(100) != 27: #27 is esc ascii code
    if cv2.getWindowProperty("image",cv2.WND_PROP_VISIBLE)<=0:
        break
