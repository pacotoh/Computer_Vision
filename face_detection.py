import numpy as np
import cv2 as cv
import time

import matplotlib.pyplot as plt

CPATH = '/home/pacotoh/anaconda3/share/OpenCV/haarcascades/'

def faceDetection(cpath, dev=0):
    cap = cv.VideoCapture(dev)
    face_cascade = cv.CascadeClassifier(cpath + 'haarcascade_frontalface_default.xml')

    while(True):
        key = cv.waitKey(1) & 0xFF
        ret, frame = cap.read()

        faces = face_cascade.detectMultiScale(frame)

        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi = frame[y:y+h, x:x+w]

        cv.imshow('face_detector', frame)

        if key == 27:
            break

    cv.destroyAllWindows()

if __name__ == "__main__":
    faceDetection(CPATH)
