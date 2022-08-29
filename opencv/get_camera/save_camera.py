import cv2

cap = cv2.VideoCapture(0)


fourcc = cv2.VideoWriter_fourcc(*'DIVX') # mac use mp4v
out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))

while cv2.waitKey(1)!=27:#esc
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)
        cv2.imshow('frame',frame)
    else:
        break
      
cap.release()
out.release()
cv2.destroyAllWindows()

