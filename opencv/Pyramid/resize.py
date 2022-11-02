import cv2
import numpy as np
img = cv2.imread("../image/Lenna.jpg")
smallImage = img.copy()
cv2.imshow("origin image",img)

smallImage = cv2.resize(img, (40, 40))

cv2.imshow("small omage",smallImage)

finalImage = smallImage.copy()
finalImage = cv2.resize(finalImage, (316, 316),interpolation=cv2.INTER_LINEAR)
  
cv2.imshow("final image",finalImage)
while cv2.waitKey(100) != 27: #27 is esc ascii code
    if cv2.getWindowProperty("final image",cv2.WND_PROP_VISIBLE)<=0:
        break
