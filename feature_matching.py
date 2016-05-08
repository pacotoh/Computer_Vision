import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import utils as ut
import os


def play(dev=0):

    cap = cv.VideoCapture(dev)
    model_index = 0
    models_path = 'images/feature_matching/models/'
    models = []  # list of the created image models
    matching = False

    method = cv.xfeatures2d.SIFT_create()
    bf = cv.BFMatcher()

    if not os.path.exists(models_path):
        os.makedirs(models_path)

    if os.path.exists(models_path + 'save.pkl'):
        matching = True
        models, model_index = ut.load_session(models_path)
        model_index += 1

    while(True):
        key = cv.waitKey(1) & 0xFF
        ret, frame = cap.read()

        # take an image to create a model
        if key == ord('m'):
            matching = True
            md = cv.flip(frame, 1)
            model_index += 1
            cv.imwrite(models_path + 'm' + str(model_index) + '.png', md)
            ut.save_session(models_path)
            print('--Created: model' + str(model_index) + '.png')

        # make the matching with the image and the models
        if key == ord('c') and matching:
            print('--Matching...')
            models, model_index = ut.load_session(models_path)

            capt = cv.flip(frame, 1)
            kpoints1, ds1 = method.detectAndCompute(capt, None)

            good = []
            model = None
            for md in models:
                kpoints2, ds2 = method.detectAndCompute(md, None)
                matches = bf.knnMatch(ds1, ds2, k=2)

                temp = []
                for m, n in matches:
                    if m.distance < 0.8*n.distance:
                        temp.append(m)
                if len(temp) > len(good):
                    good = temp
                    model = md

            sol = cv.drawMatchesKnn(capt, kpoints1,
                                    model, kpoints2, matches[:20],
                                    None, flags=2)
            cv.imshow('matching', sol)

        cv.imshow('frame', cv.flip(frame, 1))

        if key == 27:
            break

    cv.destroyAllWindows()

if __name__ == "__main__":
    play()
