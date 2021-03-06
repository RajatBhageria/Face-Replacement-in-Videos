import dlib
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def facialLandmark(img):

    predictor_path = "shape_predictor_68_face_landmarks.dat"
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) # improve image contrast
    gray = clahe.apply(gray)
    dets = detector(gray, 0)

    for k, d in enumerate(dets):
        shape = predictor(gray, d)

    vec = np.empty([68,2], dtype=int)
    for b in range(68):
        vec[b][0] = shape.part(b).x
        vec[b][1] = shape.part(b).y

    return vec

    #plot the points if need to check
    #plt.scatter(vec[:, 0], vec[:, 1])
    #plt.show()
