import cv2

def update_it(x):
  print(x)

img = cv2.imread("../image/Lenna.jpg")
cv2.namedWindow('image')

cv2.createTrackbar('bar','image',0,255,update_it)
cv2.imshow("image", img)

while cv2.waitKey(100) != 27: #27 is esc ascii code
    if cv2.getWindowProperty("image",cv2.WND_PROP_VISIBLE)<=0:
        break
