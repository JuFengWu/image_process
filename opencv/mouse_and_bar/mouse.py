import cv2


def draw_circle(event,x,y,flags,param):
    #if event == cv2.EVENT_LBUTTONDBLCLK:  
    #    cv2.circle(img,(x,y),20,(255,0,0),-1)  
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),2,(255,0,0),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img,(x,y),2,(0,0,255),-1)
    #if event == cv2.EVENT_MOUSEMOVE:
    #    cv2.circle(img,(x,y),1,(0,255,0),-1)

img = cv2.imread("../image/Lenna.jpg")
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while True: #27 is esc ascii code
    cv2.imshow("image", img)
    if  cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()


