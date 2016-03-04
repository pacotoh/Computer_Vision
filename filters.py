import utils
import cv2 as cv
import sys
from PyQt4 import QtGui, QtCore
import roi
import scipy.signal as signal
import numpy as np

# change the kernel to apply the convolve2D method
ker = np.array([[ 1, 0, 0]
               ,[ 0, 0, 0]
               ,[ 0, 0, 1]])

class Window(QtGui.QMainWindow):
    def __init__(self, roi):
        super(Window, self).__init__()
        self.setGeometry(250, 250, 500, 300)
        self.setWindowTitle('Computer Vision Filters')
        self.roi = roi
        self.home()
        self.filt = False

    def home(self):
        # buttons
        btn = QtGui.QPushButton('Original', self)
        btn.clicked.connect(self.show_img)
        btn.resize(100, 50)
        btn.move(200, 20)

        btn = QtGui.QPushButton('Box', self)
        btn.clicked.connect(self.boxFilter)
        btn.resize(100, 50)
        btn.move(50, 100)

        btn = QtGui.QPushButton('Gaussian Blur', self)
        btn.clicked.connect(self.gaussianBlur)
        btn.resize(100, 50)
        btn.move(200, 100)

        btn = QtGui.QPushButton('Median Blur', self)
        btn.clicked.connect(self.medianBlur)
        btn.resize(100, 50)
        btn.move(350, 100)

        btn = QtGui.QPushButton('Bilateral', self)
        btn.clicked.connect(self.bilateralFilter)
        btn.resize(100, 50)
        btn.move(50, 200)

        btn = QtGui.QPushButton('Laplacian', self)
        btn.clicked.connect(self.laplacianFilter)
        btn.resize(100, 50)
        btn.move(200, 200)

        btn = QtGui.QPushButton('Convolve2D', self)
        btn.clicked.connect(self.convolve2d)
        btn.resize(100, 50)
        btn.move(350, 200)

        self.show()

    # to display the original image
    def show_img(self):
        self.roi.play()

    # apply filters to the image
    # TODO crash: if we don't close the effect and try another
    def boxFilter(self):
        self.roi.play(lambda x: cv.boxFilter(x, -1, (50, 50)))

    def gaussianBlur(self):
        self.roi.play(lambda x: cv.GaussianBlur(x, (0,0), 5))

    def medianBlur(self):
        self.roi.play(lambda x: cv.medianBlur(x, 11))

    def bilateralFilter(self):
        self.roi.play(lambda x: cv.bilateralFilter(x, 0, 10, 10))

    def laplacianFilter(self):
        self.roi.play(lambda x: x+1*cv.Laplacian(x, -1))

    def convolve2d(self):
        self.roi.play(lambda x: utils.cconv(ker, utils.rgb2gray(x).astype(float)/255))

def main():
    my_roi = roi.Roi()
    app = QtGui.QApplication(sys.argv)
    GUI = Window(my_roi) # now we pass the roi to the window
    sys.exit(app.exec_())

main()
