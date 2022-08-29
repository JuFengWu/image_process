import cv2

cap = cv2.VideoCapture(0)

while cv2.waitKey(1)!=27:#esc
  
  ret, frame = cap.read()
  cv2.imshow('frame', frame)


cap.release()

cv2.destroyAllWindows()

