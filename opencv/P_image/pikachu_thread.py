import cv2

max_value = 0
min_value = 0
def update_max(x):
    global max_value 
    max_value = x
    
def update_min(x):
    global min_value 
    min_value = x
    
    
img = cv2.imread("Pikachu.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('imgGray')
cv2.createTrackbar('min','imgGray',0,255,update_min)
cv2.createTrackbar('max','imgGray',0,255,update_max)
cv2.imshow('imgGray',imgGray)

while cv2.waitKey(500)!=27: #esc
    print("min_value " + str(min_value))
    print("max_value " + str(max_value))
    _, mask = cv2.threshold(imgGray, min_value, max_value, cv2.THRESH_BINARY)
    cv2.imshow('img',mask)