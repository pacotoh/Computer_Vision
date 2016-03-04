#!/usr/bin/env python

import cv2 as cv
import os, os.path
import matplotlib.pyplot as plt
from time import gmtime, strftime
import numpy as np
import utils

class Roi():
    def __init__(self):
        ix,iy = 200,200
        jx,jy = -1, -1
        self.frame = -1
        self.roi = -1
        self.roi_capt = False
        self.isButtonDown = False

    def play(self, f=None, dev=0):
        cap = cv.VideoCapture(dev)
        pausa = False
        img_index = 0
        roi_index = 0

        #creating the time name value of the session
        time_session = strftime('%d_%m', gmtime())
        path = 'images/' + time_session + '/'

        if not os.path.exists(path + 'save.pkl'):
            img_index = 0
            roi_index = 0
        else:
            img_list,img_index = utils.load_session(path)

        while True:
            key = cv.waitKey(1) & 0xFF
            ret, self.frame = cap.read()
            #set the function mark_corner to left click
            cv.setMouseCallback('frame', self.mark_corner)

            if key == 27:
                cap.release()
                break

            if key == 32:
                pausa = not pausa

            #creates a capture
            if key == ord('c'):
                if not os.path.exists(path):
                    os.makedirs(path)
                cv.imwrite(path + '/img' + str(img_index) + '.png', self.frame)
                print('#Capture: img' + str(img_index))
                img_index+=1

            if key == ord('t') and self.roi_capt:
                cv.imwrite(path + '/roi' + '.png', self.roi)

            #saves the current session
            if key == ord('s'):
                utils.save_session(path)

            if pausa:
                continue


            if self.roi_capt:
                self.roi = self.roi_capture(self.frame,
                                      (self.ix, self.iy), (self.jx, self.jy), f, (255, 255, 255))
            cv.imshow('frame',self.frame)

        cv.destroyAllWindows()

    #function to create a roi and apply transform to it
    def roi_capture(self, frame, lu, rd, f, color=(255, 255, 255)):
        l, u = lu
        r, d = rd
        self.roi = frame[u:d, l:r]
        if self.roi.size == 0:
            isButtonDown = False
            return
        cv.rectangle(self.frame, lu, rd, color)
        if f == None:
            cv.imshow('roi_capture', self.roi)
        else:
            cv.imshow('roi_capture', f(self.roi))
        return self.roi

    #the event action
    def mark_corner(self, event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            self.ix,self.iy = x,y
            self.isButtonDown = True
        if event == cv.EVENT_LBUTTONUP and self.isButtonDown:
            self.jx,self.jy = x,y
            self.isButtonDown = False
            self.roi_capt = not self.roi_capt
