import cv2 as cv
import numpy as np
import utils

def play(dev=0):
    cap = cv.VideoCapture(dev)
    bgsub = cv.createBackgroundSubtractorMOG2(500, 50, True)
    key = 0
    pause = False

    while(True):
        key = cv.waitKey(1) & 0xFF
        ret, frame = cap.read()

        bgs = bgsub.apply(frame)

        cv.imshow('frame', cv.flip(frame, 1))
        cv.imshow('bgs', cv.flip(bgs, 1))

        b_img = bgs.astype(bool)

        print(b_img)

        if key == 27:
            break
        if key == 32:
            pause = not pause
        if pause:
            continue

    cv.destroyAllWindows()

if __name__ == "__main__":
    play()
