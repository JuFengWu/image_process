import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# For static images:
file = 'Lenna.jpg'
with mp_face_detection.FaceDetection(
    model_selection=1, min_detection_confidence=0.5) as face_detection:

    image = cv2.imread(file)
    h, w, c = image.shape
    # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
    results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Draw face detections of each face.
    if not results.detections:
        print("no result")
      
    for detection in results.detections:
        keyPoint = mp_face_detection.get_key_point(
          detection, mp_face_detection.FaceKeyPoint.LEFT_EYE )
        
        print(keyPoint.x)
        print(keyPoint.y)
        center = ( int(keyPoint.x * w), int(keyPoint.y * h))
        print(center)
        radius = 3
        color = (255,0,0)
        thickness = 2
        cv2.circle(image, center, radius, color, thickness)
    cv2.imshow('MediaPipe Face Detection', image)
    cv2.waitKey(0)
    
    
    
