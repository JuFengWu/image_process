import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
mp_holistic = mp.solutions.holistic

file = 'Lenna.jpg'
with mp_face_mesh.FaceMesh(static_image_mode=True,
    max_num_faces=1,refine_landmarks=True,min_detection_confidence=0.5) as face_mesh:

    image = cv2.imread(file)
    results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    if not results.multi_face_landmarks:
        print("no face detect")
    else:    
        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(
              image=image,
              landmark_list=face_landmarks,
              connections=mp_face_mesh.FACEMESH_TESSELATION,
              landmark_drawing_spec=None,
              connection_drawing_spec=mp_drawing_styles
              .get_default_face_mesh_tesselation_style())
            
            cv2.imshow('MediaPipe Face Detection', image)
            mp_drawing.plot_landmarks(
                face_landmarks)
            cv2.waitKey(0)
            