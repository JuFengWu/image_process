import cv2

img = cv2.imread("../image/Lenna.jpg")
cv2.circle(img,(166,166),10,(0,0,255),-1)
cv2.imwrite('save_img.png',img)