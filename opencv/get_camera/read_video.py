import cv2

cap = cv2.VideoCapture('output.mp4')

while cv2.waitKey(1)!=27:
  ret, frame = cap.read()
  cv2.imshow('frame', frame)
  cv2.waitKey(20)

cap.release()
cv2.destroyAllWindows()


