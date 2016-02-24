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
    h = cv.calcHist([yuv]     # podríamos pasar varias regiones
                    ,[1,2]    # elegimos los canales U y V
                    ,None     # posible máscara
                    ,[32,32]  # las cajitas en cada dimensión
                    ,[0,256]+[0,256] # rango de interés (todo)
                   )
    return normhist(h)

if __name__ == "__main__":
    print('main')
