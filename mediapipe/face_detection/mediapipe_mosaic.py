import cv2
import mediapipe as mp
from mosaic_function import mosaic
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# For static images:
file = 'test.png'
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
        location = detection.location_data
        relative_bounding_box = location.relative_bounding_box
        rect_start_point = (int(relative_bounding_box.xmin * w), 
                            int(relative_bounding_box.ymin * h))
        boundingBox = (int(relative_bounding_box.width*w),int(relative_bounding_box.height* h))
          
        mosaic(image,rect_start_point[0],rect_start_point[1],boundingBox[0],boundingBox[1])
          
        
    cv2.imshow('MediaPipe Face Detection', image)
    cv2.waitKey(0)


