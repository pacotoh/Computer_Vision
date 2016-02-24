import numpy             as np
import scipy.linalg      as la
import cv2               as cv
import skimage           as si
import matplotlib.pyplot as plt
import matplotlib.cm     as cm
import matplotlib.pylab  as pylab
import copy
from matplotlib.pyplot import imshow, subplot, title
import utils

def uvh(x):
    def normhist(x):
        return x / np.sum(x)

    yuv = utils.rgb2yuv(x)
    h = cv.calcHist([yuv]
                    ,[1,2]
                    ,None
                    ,[32,32]
                    ,[0,256]+[0,256]
                   )
    return normhist(h)

if __name__ == "__main__":
    print('main')
