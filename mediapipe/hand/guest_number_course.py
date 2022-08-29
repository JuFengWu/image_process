import cv2
import mediapipe as mp
import random
from hand_meaning import hand_pos, hand_angle
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

while(True):
  frame = get_camera_image()
  with mp_hands.Hands(
      static_image_mode=True,max_num_hands=2,
      min_detection_confidence=0.5) as hands:
      results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))