import cv2
import mediapipe as mp
import random
from hand_meaning import hand_pos, hand_angle
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

#random
value = random.randint(1, 4)
#獲得影像
image = cv2.imread("one.png")
image.shape
w = image.shape[0]
h = image.shape[1]
#影像處理
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:

    image = cv2.flip(image, 1)
    # Convert the BGR image to RGB before processing.
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    #獲得結論
    fingerPoints = []  
    for i in results.multi_hand_landmarks[0].landmark:
      
      x = i.x*w
      y = i.y*h
      fingerPoints.append((x,y))
    
    #計算手指頭角度
    fingerAngle = hand_angle(fingerPoints)
    mp_drawing.draw_landmarks(
          image,
          results.multi_hand_landmarks[0],
          mp_hands.HAND_CONNECTIONS,
          mp_drawing_styles.get_default_hand_landmarks_style(),
          mp_drawing_styles.get_default_hand_connections_style())
    #從角度獲得手部姿勢意思
    meaning = hand_pos(fingerAngle)
    print("your value is " + meaning)
    print("random valuse is " + str(value))
    if(str(value) == meaning):
      print("you win")
    else :
      print("you lost")
    cv2.imshow("image",image)
    cv2.waitKey(0)