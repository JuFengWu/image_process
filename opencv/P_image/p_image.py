import cv2

def put_item(image,itemSize,itemCenter,changeItem):
    item = cv2.resize(changeItem, (itemSize, itemSize))
    itemGray = cv2.cvtColor(item, cv2.COLOR_BGR2GRAY)
    _, itemMask = cv2.threshold(itemGray, 253, 255, cv2.THRESH_BINARY)
    cv2.imshow("itemMask",itemMask)
    height, width, _ = item.shape
    originX, originY = int(itemCenter[0]-width/2), int(itemCenter[1]-height/2)
    itemArea = image[originY: originY+height, originX: originX+width]
    noPicImg = cv2.bitwise_and(itemArea, itemArea, mask=itemMask)
    cv2.imshow("noPicImg",noPicImg)
    mask_inv = cv2.bitwise_not(itemMask)
    itemFinal = cv2.bitwise_and(item, item, mask=mask_inv)
    cv2.imshow("itemFinal",itemFinal)
    finalArea = cv2.add(noPicImg,itemFinal)
    cv2.imshow("finalArea",finalArea)
    image[originY: originY+height, originX: originX+width] = finalArea
    
    
changeItem = cv2.imread("pikachu.png")
lennaImg = cv2.imread("Lenna.jpg")
put_item(lennaImg,66,(283,283),changeItem)

cv2.imshow("lennaImg",lennaImg)
cv2.waitKey(0)