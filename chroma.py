#!/usr/bin/env python

import cv2 as cv
import numpy as np
import utils

# global variables
re = cv.imread('images/chroma/pano002.jpg') # the new background
LIMIT = 65 # mask limit
BACK_PATH = 'images/chroma/background.png' # path of the chroma bg

# auxiliar method to apply the mask
def apply_mask(dif_img, img, dst):
    global LIMIT
    mask = dif_img > LIMIT
    r,c = mask.shape
    res = cv.resize(dst,(c,r))
    mask3 = mask.reshape(r,c,1)
    np.copyto(res,img, where = mask3)
    cv.imshow('res', res)

# chroma using the rgb or yub images
def chroma_rgb(bg, img, dst):
    drgb = np.sum(abs(img.astype(float)-bg.astype(float)),2)
    apply_mask(drgb, img, dst)

def chroma_yuv(bg, img, dst):
    obuv = img.astype(float)[:,:,[1,2]]
    bkuv = bg.astype(float)[:,:,[1,2]]
    duv = np.sum(abs(obuv-bkuv),2)
    apply_mask(duv, img, dst)

# chroma in a photo
def static_chroma(bg, img, dst):
    cv.imwrite('images/chroma/res.png',chroma_rgb(bg, img, dst))

# b takes the chroma's background
# c starts the chroma's effect
def play(dev=0):
    cap = cv.VideoCapture(dev)
    key = 0
    pause = False
    bg = False
    chroma_go = False
    global LIMIT

    while(True):
        key = cv.waitKey(1) & 0xFF
        ret, frame = cap.read()

        if key == 27:
            break
        if key == 32:
            pause = not pause
        if pause:
            continue

        if key == ord('b'):
            cv.imwrite(BACK_PATH, frame)
            bg = True

        if key == ord('c') and bg:
            back = cv.imread(BACK_PATH)
            chroma_go = True

        if key == ord('+'):
            LIMIT = LIMIT + 5

        if key == ord('-'):
            LIMIT = LIMIT - 5

        if chroma_go:
            chroma_yuv(back, frame, re)
        else:
            cv.imshow('frame', cv.flip(frame, 1))
    cv.destroyAllWindows()

if __name__ == "__main__":
    play()
