import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import utils as ut

def play(dev=0):
    cap = cv.VideoCapture(dev)
    model_index = 0
    models_path = 'images/feature_matching/models/'
    tests_path = 'images/feature_matching/tests/'
    models = []
    tests = [] # list of the created image models

    if os.path.exists(models_path + 'save.pkl'):
        models, num_models = ut.load_session(models_path)
        print(num_models)

    while(True):
        key = cv.waitKey(1) & 0xFF
        ret, frame = cap.read()

        if key == ord('m'):
            md = cv.flip(frame, 1)
            cv.imwrite(models_path + 'm' + str(model_index) + '.png', md)
            model_index+=1

        if key == ord('c'):
            capt = cv.flip(frame, 1)
            # do the matching here

        cv.imshow('frame', frame)

        if key == 27:
            break

    cv.destroyAllWindows()
    ut.save_session(models_path)

if __name__ == "__main__":
    play()
