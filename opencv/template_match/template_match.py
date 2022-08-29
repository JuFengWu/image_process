import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('hand_1.png')
img2 = img.copy()
template = cv2.imread('hand_template.png')
w = template.shape[1]
h = template.shape[0]

img = img2.copy()
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)
topLeft = maxLoc
bottomRight = (topLeft[0] + w, topLeft[1] + h)
cv2.rectangle(img,topLeft, bottomRight, 255, 2)
cv2.imshow('result_img',img)
cv2.waitKey(0)