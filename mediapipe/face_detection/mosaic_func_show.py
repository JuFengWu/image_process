import cv2
from mosaic_function import mosaic


if __name__ == "__main__":

  img = cv2.imread('Lenna.jpg')
  x = 140   #left up x
  y = 120   #left up y
  cw = 100  
  ch = 120
  mosaic(img,x,y,cw,ch)
  cv2.imshow('mosaic', img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

