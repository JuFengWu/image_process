import cv2
import mediapipe as mp
import random
from hand_meaning import hand_pos, hand_angle
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
w, h = 640, 480

while True:
  
  ret, frame = cap.read()
  frame = cv2.resize(frame, (w,h))
  with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
    frame= cv2.flip(frame,1)
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if(results.multi_hand_landmarks == None): # for protection
      print("no hand")
      cv2.imshow('frame', frame)
      key = cv2.waitKey(1)
      if(key==27):
        break
    else :
      for hand_landmarks in results.multi_hand_landmarks: 
        showPoint = mp_hands.HandLandmark.INDEX_FINGER_TIP
        xPoint = hand_landmarks.landmark[showPoint].x * w
        yPoint = hand_landmarks.landmark[showPoint].y * h
        frame = cv2.circle(frame, (int(xPoint),int(yPoint)), 5, (255,0,0), -1)
      cv2.imshow('frame', frame)
      key = cv2.waitKey(1)
      if(key==27):
        break
        
        