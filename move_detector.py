import cv2 as cv
import numpy as np
import utils
import os

MAX_BGS = 15000 # number of pixels(x, y)*255 : white
MAX_FRAMES = 10 # frames to detect the movement
path = 'images/move_detector/'

def play(dev=0):
    cap = cv.VideoCapture(dev)
    # Background subtractor with default parameters: history = 500,
    # varThreshold = 16 and detectShadows = True
    bgsub = cv.createBackgroundSubtractorMOG2(500, 16, False)
    key = 0
    pause = False
    list_frames = []
    img_index = 0

    while(True):
        key = cv.waitKey(1) & 0xFF
        ret, frame = cap.read()

        bgs = bgsub.apply(frame)
        bgs_count = sum(sum(bgs))
        print(bgs_count)

        if bgs_count > MAX_BGS:
            list_frames.append(frame)

        if len(list_frames) > MAX_FRAMES:
            cv.imwrite(path + 'capt' + str(img_index) + '.png', cv.flip(frame, 1))
            img_index+=1
            list_frames = []

        cv.imshow('frame', cv.flip(bgs, 1))

        if key == 27:
            break
        if key == 32:
            pause = not pause
        if pause:
            continue

    cv.destroyAllWindows()

if __name__ == "__main__":
    play()
