import cv2

max_value = 0
min_value = 0
def update_max(x):
    global max_value 
    max_value = x
    
def update_min(x):
    global min_value 
    min_value = x
    
    
img = cv2.imread("star.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('img')
cv2.createTrackbar('min','img',0,255,update_min)
cv2.createTrackbar('max','img',0,255,update_max)

while cv2.waitKey(500)!=27: #esc
    print("min_value " + str(min_value))
    print("max_value " + str(max_value))
    _, mask = cv2.threshold(imgGray, min_value, max_value, cv2.THRESH_BINARY)
    cv2.imshow('img',mask)