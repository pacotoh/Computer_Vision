import numpy as np
import cv2 as cv
import time

import matplotlib.pyplot as plt

CPATH = '/home/pacotoh/anaconda3/share/OpenCV/haarcascades/'

# we have a dictionary with the filters to apply
filter_dict = {0: None,
               1: lambda x: cv.boxFilter(x, -1, (50, 50)),
               2: lambda x: cv.GaussianBlur(x, (0,0), 5),
               3: lambda x: cv.medianBlur(x, 11),
               4: lambda x: x+1*cv.Laplacian(x, -1)}

color_maps = [cv.COLORMAP_AUTUMN, cv.COLORMAP_WINTER, cv.COLORMAP_SUMMER, cv.COLORMAP_SPRING]
stage_index = ['o', 'i', 'v', 'p']

def face_detection(cpath, dev=0):
    cap = cv.VideoCapture(dev)
    face_cascade = cv.CascadeClassifier(cpath + 'haarcascade_frontalface_default.xml')
    f = None
    color = None

    while(True):
        key = cv.waitKey(1) & 0xFF
        ret, frame = cap.read()
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        if key in [ord(x) for x in stage_index]:
            color = color_maps[stage_index.index(chr(key))]

        if key == 27:
            break

        if not key == 255 and key-48 < len(filter_dict):
            f = filter_dict[key-48]

        faces = face_cascade.detectMultiScale(frame_gray, 1.2, 3)

        for (x, y, w, h) in faces:
            roi = frame[y:y+h, x:x+w]
            # we can only apply the filter if the roi exists
            if roi is not None and f is not None:
                frame[y:y+h, x:x+w] = f(frame[y:y+h, x:x+w])
            # to apply a colorMap to the roi
            if color is not None:
                frame[y:y+h, x:x+w] = cv.applyColorMap(frame[y:y+h, x:x+w], color)

        cv.imshow('face_detector', frame)

    cv.destroyAllWindows()

if __name__ == "__main__":
    face_detection(CPATH)
