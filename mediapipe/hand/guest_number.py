import cv2
import mediapipe as mp
import random
from hand_meaning import hand_pos, hand_angle
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
w, h = 640, 480
computerValue = random.randint(0, 9)
print("computerValue is " + str(computerValue))
while True:
  
  ret, frame = cap.read()
  frame = cv2.resize(frame, (w,h))
  with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
    frame= cv2.flip(frame,1)
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    fingerPoints = []                   # 記錄手指節點座標的串列
    for i in results.multi_hand_landmarks[0].landmark:
      
      x = i.x*w
      y = i.y*h
      fingerPoints.append((x,y))
    
    mp_drawing.draw_landmarks(
          frame,
          results.multi_hand_landmarks[0],
          mp_hands.HAND_CONNECTIONS,
          mp_drawing_styles.get_default_hand_landmarks_style(),
          mp_drawing_styles.get_default_hand_connections_style())
    fingerAngle = hand_angle(fingerPoints)

    meaning = hand_pos(fingerAngle)
    print("your value is " + meaning)
    cv2.putText(frame, meaning, (30,120), cv2.FONT_HERSHEY_SIMPLEX , 1, (255,255,255), 1, cv2.LINE_AA)
    if meaning == str(computerValue):
        cv2.putText(frame, "Correct", (30,160), cv2.FONT_HERSHEY_SIMPLEX , 1, (255,255,255), 1, cv2.LINE_AA)
        cv2.putText(frame, "Press C to change value", (30,190), cv2.FONT_HERSHEY_SIMPLEX , 1, (255,255,255), 1, cv2.LINE_AA)
    else:
        cv2.putText(frame, "No Correct", (30,160), cv2.FONT_HERSHEY_SIMPLEX , 1, (255,255,255), 1, cv2.LINE_AA)
    
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if(key==27):
        break
    elif (key == 67 or key == 99):
        computerValue = random.randint(0, 9)
        print("computerValue is " + str(computerValue))