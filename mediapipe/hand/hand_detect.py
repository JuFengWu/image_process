import cv2
import mediapipe as mp
from mpl_toolkits.mplot3d import Axes3D
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

file = 'hand.png'
with mp_hands.Hands(
    static_image_mode=True,max_num_hands=2,
    min_detection_confidence=0.5) as hands:

    image = cv2.imread(file)
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Print handedness and draw hand landmarks on the image.
    print('Handedness:', results.multi_handedness)
    image_height, image_width, _ = image.shape
    for hand_landmarks in results.multi_hand_landmarks: # 兩隻手，畫兩次
          mp_drawing.draw_landmarks(
              image,hand_landmarks,mp_hands.HAND_CONNECTIONS,
              mp_drawing_styles.get_default_hand_landmarks_style(),
              mp_drawing_styles.get_default_hand_connections_style())
     
    key = cv2.waitKey(0)     
    cv2.imshow('detect hand',image)
    cv2.waitKey(0)
