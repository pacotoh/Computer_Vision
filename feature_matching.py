import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import utils as ut
import os
import pickle

def play(dev=0):

    cap = cv.VideoCapture(dev)
    model_index = 0
    models_path = 'images/feature_matching/models/'
    tests_path = 'images/feature_matching/tests/'
    models = []
    tests = [] # list of the created image models
    save = False
    load = False

    while(True):
        key = cv.waitKey(1) & 0xFF
        ret, frame = cap.read()

        if os.path.exists(models_path + 'save.pkl'):
            load = True

        # load the number of models and the models
        if key == ord('l') and load:
            save = True
            models, ind = ut.load_session(models_path)
            print(ind)

        if key == ord('s')and save:
            ut.save_session(models_path)

        # take an image to make a model of it
        if key == ord('m'):
            save = True
            md = cv.flip(frame, 1)
            cv.imwrite(models_path + 'm' + str(model_index) + '.png', md)
            model_index+=1

        # make the matching with the image and the models
        if key == ord('c') and load:
            capt = cv.flip(frame, 1)
            # do the matching here
            

        cv.imshow('frame', frame)

        if key == 27:
            break

    cv.destroyAllWindows()

if __name__ == "__main__":
    play()
