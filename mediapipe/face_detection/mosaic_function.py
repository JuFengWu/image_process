import cv2

def mosaic(img, x,y,cw,ch):
  mosaic = img[y:y+ch, x:x+cw]   
  level = 15         
  h = int(ch/level)  
  w = int(cw/level)  
  mosaic = cv2.resize(mosaic, (w,h), interpolation=cv2.INTER_LINEAR)
  mosaic = cv2.resize(mosaic, (cw,ch), interpolation=cv2.INTER_NEAREST)
  img[y:y+ch, x:x+cw] = mosaic

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
