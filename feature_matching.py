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
    models = [] # list of the created image models
    save = False
    load = False
    matching = False

    #akaze = cv.AKAZE_create()
    #bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck = True)
    method = cv.xfeatures2d.SIFT_create()
    bf = cv.BFMatcher()

    while(True):
        key = cv.waitKey(1) & 0xFF
        ret, frame = cap.read()

        if os.path.exists(models_path + 'save.pkl'):
            load = True
            matching = True
            models, model_index = ut.load_session(models_path)

        # load the number of models and the models
        if key == ord('l') and load:
            save = True
            models, ind = ut.load_session(models_path)

        if key == ord('s')and save:
            ut.save_session(models_path)

        # take an image to create a model
        if key == ord('m'):
            save = True
            md = cv.flip(frame, 1)
            cv.imwrite(models_path + 'm' + str(model_index) + '.png', md)
            model_index+=1

        # make the matching with the image and the models
        if key == ord('c') and matching:
            models, ind = ut.load_session(models_path)

            capt = cv.flip(frame, 1)
            md = models[1]
            kpoints1, ds1 = method.detectAndCompute(capt, None)
            #kpoints2, ds2 = method.detectAndCompute(md, None)
#####
            good = []
            model = None
            for md in models:
                kpoints2, ds2 = method.detectAndCompute(md, None)
                matches = bf.knnMatch(ds1, ds2, k = 2)

                temp = []
                for m,n in matches:
                    if m.distance < 0.8*n.distance:
                        temp.append(m)
                if len(temp) > len(good):
                    good = temp
                    model = md
#####
            #matches = bf.knnMatch(ds1, ds2, k = 2)

            #good = []
            #for m,n in matches:
            #    if m.distance < 0.8*n.distance:
            #        good.append(m)
            #print(len(good))

            # don't draw single points
            #sol = cv.drawMatchesKnn(capt, kpoints1, md, kpoints2, matches[:15], None, flags = 2)
            sol = cv.drawMatchesKnn(capt, kpoints1, model, kpoints2, matches, None, flags = 2)
            cv.imshow('sol', sol)

        cv.imshow('frame', cv.flip(frame, 1))

        if key == 27:
            break

    cv.destroyAllWindows()

if __name__ == "__main__":
    play()
