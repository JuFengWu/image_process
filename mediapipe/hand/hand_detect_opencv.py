import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

iamgeFile = 'hand_1.png'

with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
    
    image = cv2.flip(cv2.imread(iamgeFile), 1)
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Print handedness and draw hand landmarks on the image.
    print('Handedness:', results.multi_handedness)
    if not results.multi_hand_landmarks:
      print('there is no hands')
    image_height, image_width, _ = image.shape
    i = 0
    for hand_landmarks in results.multi_hand_landmarks:
      print('hand_landmarks:', hand_landmarks)
      #showPoint = 0
      showPoint = mp_hands.HandLandmark.WRIST
      xPoint = hand_landmarks.landmark[showPoint].x * image_width
      yPoint = hand_landmarks.landmark[showPoint].y * image_height
      print(len(hand_landmarks.landmark))
      print("hand is "+ results.multi_handedness[i].classification[0].label)# show left hand or right hand
      image = cv2.circle(image, (int(xPoint),int(yPoint)), 5, (255,0,0), -1)
      cv2.imshow('image',image)
      key = cv2.waitKey(0)
      i = i+1
      
    print("hand number is " + str(i))
