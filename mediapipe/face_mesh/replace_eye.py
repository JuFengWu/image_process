import cv2
import mediapipe as mp
import math
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

def get_eye_size_and_center(faceLandmarks, maxPoints, w, h):
    
    eyePoint = []
    for index in maxPoints:
        x = int(faceLandmarks.landmark[index].x * w)
        y = int(faceLandmarks.landmark[index].y * h)
        eyePoint.append([x,y])
    eyeLength = int(math.pow(math.pow((eyePoint[0][0] - eyePoint[1][0]), 2) + 
                math.pow((eyePoint[0][1] - eyePoint[1][1]), 2), 0.5))
    eyeCenter = [int((eyePoint[0][0] + eyePoint[1][0])/2),int((eyePoint[0][1] + eyePoint[1][1])/2)]
    return eyeLength,eyeCenter
    
def put_item_to_eye(image,eyeSize,eyeCenter,changeItem):
    eye = cv2.resize(changeItem, (eyeSize, eyeSize))
    eyeGray = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY)
    _, eyeMask = cv2.threshold(eyeGray, 218, 255, cv2.THRESH_BINARY)
    height, width, _ = eye.shape
    originX, originY = int(eyeCenter[0]-width/2), int(eyeCenter[1]-height/2)
    eyeArea = image[originY: originY+height, originX: originX+width]
    noEyeImg = cv2.bitwise_and(eyeArea, eyeArea, mask=eyeMask)
    mask_inv = cv2.bitwise_not(eyeMask)
    eyeFinal = cv2.bitwise_and(eye, eye, mask=mask_inv)
    finalEye = cv2.add(noEyeImg,eyeFinal)
    image[originY: originY+height, originX: originX+width] = finalEye
    
leftEyeMaxPoint = [33, 133]
rightEyeMaxPoint = [362, 263]

changeItem = cv2.imread("star.png")
file = 'Lenna.jpg'

with mp_face_mesh.FaceMesh(static_image_mode=True,
    max_num_faces=1,refine_landmarks=True,min_detection_confidence=0.5) as face_mesh:
    image = cv2.imread(file)
    h, w, d = image.shape
    results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    leftEyeSize,leftEyeCenter = get_eye_size_and_center(results.multi_face_landmarks[0],leftEyeMaxPoint, w, h)
    rightEyeSize,rightEyeCenter = get_eye_size_and_center(results.multi_face_landmarks[0],rightEyeMaxPoint, w , h)
    put_item_to_eye(image,leftEyeSize,leftEyeCenter,changeItem)
    put_item_to_eye(image,rightEyeSize,rightEyeCenter,changeItem)
    cv2.imshow("finish image",image)
    cv2.waitKey(0)