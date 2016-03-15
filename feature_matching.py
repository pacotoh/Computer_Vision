import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import utils as ut
import os
import pickle
import utils as ut

# TODO: Convert to gray the images?

def play(dev=0):

    cap = cv.VideoCapture(dev)
    model_index = 0
    path = 'images/feature_matching/'
    models_path = 'images/feature_matching/models/'

    models = [] # list of the created image models
    imgs = [] # list of the modeled images

    if not os.path.exists(path):
        os.makedirs(models_path)

    method = cv.xfeatures2d.SIFT_create()
    bf = cv.BFMatcher()

    # First time we test if exists the models and charge them
    if os.path.exists(path + 'models.pkl'):
        models = pickle.load(open(path + 'models.pkl', 'rb'))
        imgs = pickle.load(open(path + 'images.pkl', 'rb'))

    while(True):
        key = cv.waitKey(1) & 0xFF
        ret, frame = cap.read()

        # load the models and the images
        if key == ord('l'):
            # Testing one of them we have both for sure (models, imgs)
            if os.path.exists(path + 'models.pkl'):
                models = pickle.load(open(path + 'models.pkl', 'rb'))
                imgs = pickle.load(open(path + 'images.pkl', 'rb'))

        # We have 2 lists: models and images
        # apply detectAndCompute to each image and save it in models
        if key == ord('s'):
            for f in os.listdir(models_path):
                print(f)
                img = cv.imread(models_path + f)
                cv.imshow('img', img)
                #detect and compute the image
                kpoints, ds = method.detectAndCompute(img, None)
                # TODO: Serialize the Keypoints
                # http://hanzratech.in/2015/01/16/saving-and-loading-keypoints-in-file-using-opencv-and-python.html
                for kp in kpoints:
                    tmp = (kp.pt, kp.size, kp.angle, kp.response, kp.octave,
                            kp.class_id, desc)

                #print(kpoints)
                models.append((kpoints, ds))
                imgs.append(img)
            pickle.dump(models, open(path + 'models.pkl', 'wb'))
            pickle.dump(imgs, open(path + 'images.pkl', 'wb'))

        # Take an image to create a model
        if key == ord('m'):
            md = cv.flip(frame, 1)
            md_gray = cv.cvtColor(md, cv.COLOR_RGB2GRAY)
            cv.imwrite(models_path + 'm' + str(model_index) + '.png', md)
            kpoints, ds = method.detectAndCompute(md_gray, None)
            models.append((kpoints, ds))
            imgs.append(md)
            model_index+=1

        # make the matching with the image and the models
        if key == ord('c'):
            capt = cv.flip(frame, 1)
            kpoints1, ds1 = method.detectAndCompute(capt, None)

            good = []
            model = None
            index = 0
            for kp, ds in models:
                matches = bf.knnMatch(ds1, ds, k = 2)
                temp = []
                for m,n in matches:
                    if m.distance < 0.8*n.distance:
                        temp.append(m)
                if len(temp) > len(good):
                    good = temp
                    model = imgs[index]
                    index += 1

            sol = cv.drawMatchesKnn(capt, kpoints1, model, models[index][0], matches[:15], None, flags = 2)
            cv.imshow('sol', sol)

        cv.imshow('frame', cv.flip(frame, 1))

        if key == 27:
            break

    cv.destroyAllWindows()

if __name__ == "__main__":
    play()
