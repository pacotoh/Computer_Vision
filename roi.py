#!/usr/bin/env python

import cv2 as cv
import pickle
import os, os.path
import matplotlib.pyplot as plt
from time import gmtime, strftime
import numpy as np

#global variables for the roi creation
ix,iy = 200,200
jx,jy = -1, -1
frame = -1
roi_capt = False
isButtonDown = False

def play(f, dev=0):
    cap = cv.VideoCapture(dev)
    pausa = False
    #roi_capt = False
    img_index = 0
    roi_index = 0

    #creating the time name value of the session
    time_session = strftime('%d_%m', gmtime())
    path = 'images/' + time_session + '/'

    if not os.path.exists(path + 'save.pkl'):
        img_index = 0
        roi_index = 0
    else:
        img_list,img_index = load_session(path)

    while True:
        key = cv.waitKey(1) & 0xFF
        ret, frame = cap.read()
        #set the function mark_corner to left click
        cv.setMouseCallback('frame', mark_corner)

        if key == 27:
            cap.release()
            break

        if key == 32:
            pausa = not pausa

        #creates a capture
        if key == ord('c'):
            if not os.path.exists(path):
                os.makedirs(path)
            cv.imwrite(path + '/img' + str(img_index) + '.png', frame)
            print('#Capture: img' + str(img_index))
            img_index+=1

        if key == ord('t') and roi_capt:
            cv.imwrite(path + '/roi' + '.png', roi)

        #saves the current session
        if key == ord('s'):
            save_session(path)
            print('#Saved in ' + path + 'save.pkl')

        if pausa:
            continue

        if roi_capt:
            roi = roi_capture(f, frame, (ix, iy), (jx, jy))

        cv.imshow('frame',frame)
    cv.destroyAllWindows()

#functions to write and load pickles
def save_session(path):
    list_img = []
    for f in os.listdir(path):
        img = cv.imread(path + f)
        list_img.append(img)
    pickle.dump(list_img, open(path + 'save.pkl', 'wb'))

def load_session(path):
    list_img = pickle.load(open(path + 'save.pkl', 'rb'))
    return list_img, len(list_img)-1

#function to create a roi and apply transform to it
def roi_capture(transform, frame, lu, rd, color=(255, 255, 255)):
    l, u = lu
    r, d = rd
    roi = frame[u:d, l:r]
    if roi.size == 0:
        isButtonDown = False
        return
    cv.rectangle(frame, lu, rd, color)
    cv.imshow('roi_capture', transform(roi))
    return roi

#the event action
def mark_corner(event, x, y, flags, param):
    global isButtonDown
    global ix,iy,roi_capt
    global jx,jy
    if event == cv.EVENT_LBUTTONDOWN:
        ix,iy = x,y
        isButtonDown = True
    if event == cv.EVENT_LBUTTONUP and isButtonDown:
        jx,jy = x,y
        isButtonDown = False
        roi_capt = not roi_capt

if __name__ == "__main__":
    #save_session('./images/14_02/')
    #lst, ln = load_session('./images/14_02/')
    #print(ln)
    play(lambda x: 255 - cv.cvtColor(x, cv.COLOR_RGB2GRAY), 0)
