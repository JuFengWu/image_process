import cv2

img = cv2.imread("Lenna.jpg")
cv2.imshow("image",img)
while cv2.waitKey(100)!= 27:
    if cv2.getWindowProperty("image",cv2.WND_PROP_VISIBLE)<=0:
         break
print("end program")