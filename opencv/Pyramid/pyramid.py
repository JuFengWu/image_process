import cv2
import numpy as np
img = cv2.imread("../image/Lenna.jpg")
smallImage = img.copy()
cv2.imshow("origin image",img)

for i in range(3):
  smallImage = cv2.pyrDown(smallImage)

cv2.imshow("small omage",smallImage)

finalImage = smallImage.copy()
for i in range(3):
  finalImage = cv2.pyrUp(finalImage)
  
cv2.imshow("final image",finalImage)
while cv2.waitKey(100) != 27: #27 is esc ascii code
    if cv2.getWindowProperty("final image",cv2.WND_PROP_VISIBLE)<=0:
        break
