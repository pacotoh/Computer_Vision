import os
import cv2 as cv
import pickle
import matplotlib.cm as cm
from matplotlib.pyplot import imshow, subplot, title
from scipy import signal

#########################################################################################
############################### IMAGES ##################################################
#########################################################################################

def figsize(h=6, v=4):
    pylab.rcParams['figure.figsize'] = h,v

def readrgb(file):
    return cv.cvtColor( cv.imread("images/chroma/"+file), cv.COLOR_BGR2RGB)

def rgb2yuv(x):
    return cv.cvtColor(x,cv.COLOR_RGB2YUV)

def rgb2gray(x):
    return cv.cvtColor(x, cv.COLOR_RGB2GRAY)

def gray2float(x):
    return x.astype(float) / 255

def imshowg(x):
    imshow(x, cmap = cm.gray)

def imshowf(x):
    imshow(x, cmap = cm.gray, vmin = 0, vmax = 1)

def imshows(x, r=1):
    imshow(x, cmap = cm.gray, vmin = -r, vmax = r)

def conv(k,x):
    return cv.filter2D(x, -1, k)

def cconv(k, x):
    return signal.convolve2d(x, k, boundary='symm', mode='same')

def ft(x):
    return fft.fft2(x)

def ift(x):
    return fft.ifft2(x)

#########################################################################################
############################### PICKLES #################################################
#########################################################################################

def save_session(path):
    if os.path.exists(path):
        list_img = []
        for f in os.listdir(path):
            img = cv.imread(path + f)
            list_img.append(img)
        pickle.dump(list_img, open(path + 'save.pkl', 'wb'))

def load_session(path):
    if os.path.exists(path):
        list_img = pickle.load(open(path + 'save.pkl', 'rb'))
        return list_img, len(list_img)-1
    else:
         return -1, -1
