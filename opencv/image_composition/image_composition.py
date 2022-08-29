import cv2
import numpy as np

img1 = cv2.imread("../image/lena_left.png")
img2 = cv2.imread("../image/lena_right.png")
sift = cv2.xfeatures2d.SIFT_create()
grayImage1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
grayImage2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
kp1,des1 = sift.detectAndCompute(grayImage1,None)
kp2,des2 = sift.detectAndCompute(grayImage2,None)

#cv2.imshow('key point image',cv2.drawKeypoints(img1,kp1,None))
#cv2.waitKey(0)

match = cv2.BFMatcher()
matches = match.knnMatch(des1,des2,k=2)

googdDistance = 0.03
good = []
for m,n in matches:
    if m.distance < googdDistance*n.distance:
        good.append(m)
        
draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   flags = 2)
img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)
cv2.imshow("original_image_drawMatches.jpg", img3)
cv2.waitKey(0)

MIN_MATCH_COUNT = 10 
if len(good) > MIN_MATCH_COUNT: 
  src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2) 
  dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2) 
  M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0) 
  h,w = grayImage1.shape 
  pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2) 
  dst = cv2.perspectiveTransform(pts, M) 
  grayImage1 = cv2.polylines(grayImage1,[np.int32(dst)],True,255,3, cv2.LINE_AA) 
  cv2.imshow("grayImage1", grayImage1) 
  cv2.waitKey(0)
else: 
  print("Not enought matches are found - %d/%d", (len(good)/MIN_MATCH_COUNT))


dst = cv2.warpPerspective(img1,M,(img2.shape[1] + img1.shape[1], img2.shape[0])) 
dst[0:img2.shape[0],0:img2.shape[1]] = img2 
cv2.imshow("original_image_stitched.jpg", dst) 

def trim(frame): #crop top 
  if not np.sum(frame[0]): 
    return trim(frame[1:]) #crop top 
  if not np.sum(frame[-1]): 
    return trim(frame[:-2]) #crop top 
  if not np.sum(frame[:,0]): 
    return trim(frame[:,1:]) #crop top 
  if not np.sum(frame[:,-1]): return trim(frame[:,:-2]) 
  return frame 
  
cv2.imshow("original_image_stitched_crop.jpg", trim(dst))

cv2.waitKey(0)