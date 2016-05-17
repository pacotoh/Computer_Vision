import numpy as np
import cv2 as cv
import time

import matplotlib.pyplot as plt

CPATH = '/home/pacotoh/anaconda3/share/OpenCV/haarcascades/'

def faceDetection(cpath, f=None, dev=0):
    cap = cv.VideoCapture(dev)

    face_cascade = cv.CascadeClassifier(cpath + 'haarcascade_frontalface_default.xml')

    while(True):
        key = cv.waitKey(1) & 0xFF
        ret, frame = cap.read()
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(frame_gray, 1.2, 3)

        for (x, y, w, h) in faces:
            roi = frame[y:y+h, x:x+w]
            if roi is not None:
                frame[y:y+h, x:x+w] = f(frame[y:y+h, x:x+w])

        cv.imshow('face_detector', frame)

        if key == 27:
            break

    cv.destroyAllWindows()

if __name__ == "__main__":
    faceDetection(CPATH, lambda x: cv.Laplacian(x, -1))
