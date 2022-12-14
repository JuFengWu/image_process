import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# For static images:
file = 'Lenna.jpg'
face_detection = mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5)
#Use 0 to select a short-range model that works best for faces within 2 meters from the camera
#and 1 for a full-range model best for faces within 5 meters

image = cv2.imread(file)
    # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Draw face detections of each face.
if not results.detections:
    print("no result")
      
for detection in results.detections:
    print('Nose tip:')
    print(mp_face_detection.get_key_point(
      detection, mp_face_detection.FaceKeyPoint.NOSE_TIP))
    mp_drawing.draw_detection(image, detection)
cv2.imshow('MediaPipe Face Detection', image)
cv2.waitKey(0)
    
    
    
