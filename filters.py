import utils
import cv2 as cv
import sys
from PyQt4 import QtGui, QtCore
import roi
import scipy.signal as signal
import numpy as np

IMAGE_PATH = 'images/chroma/pano002.jpg'
image = None
gray = False
smooth = 5

# change the kernel to apply the convolve2D method
ker = np.array([[ 1, 0, 0]
               ,[ 0, 0, 0]
               ,[ 0, 0, 1]])

# we can pass the image from the command line
if len(sys.argv) == 2:
    IMAGE_PATH = sys.argv[1]

image = cv.imread(IMAGE_PATH)

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(250, 250, 500, 500)
        self.setWindowTitle('Computer Vision Filters')
        self.home()

    def home(self):
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

        btn = QtGui.QPushButton('+', self)
        btn.clicked.connect(self.plusSmooth)
        btn.resize(50, 50)
        btn.move(150, 300)

        btn = QtGui.QPushButton('-', self)
        btn.clicked.connect(self.minusSmooth)
        btn.resize(50, 50)
        btn.move(300, 300)

        checkBox = QtGui.QCheckBox('ToGray', self)
        checkBox.stateChanged.connect(self.toGray)

        self.show()

    # to display the original image
    def show_img(self):
        cv.imshow('img', image)

    # apply filters to the image
    def boxFilter(self):
        cv.imshow('boxFilter', cv.boxFilter(image, -1, (50, 50)))

    def gaussianBlur(self):
        cv.imshow('gaussianBlur', cv.GaussianBlur(image, (0,0), 5))

    def medianBlur(self):
        cv.imshow('medianBlur', cv.medianBlur(image, 11))

    def bilateralFilter(self):
        cv.imshow('bilateralFilter', cv.bilateralFilter(image, 0, 10, 10))

    def laplacianFilter(self):
        cv.imshow('laplacianFilter', image+1*cv.Laplacian(image, -1))

    def convolve2d(self):
        if gray:
            cv.imshow('convolve2D', utils.cconv(ker, image.astype(float)/255))
        else:
            QtGui.QMessageBox.about(self, 'Alert!',
            "You can't use convolve2d in a RGB image!\nHint: check 'ToGray'")

    def plusSmooth(self):
        global smooth
        smooth = smooth*2

    def minusSmooth(self):
        global smooth
        smooth = smooth/2

    # if checked: we have a gray image
    def toGray(self, state):
        global image, gray
        if state == QtCore.Qt.Checked:
            image = utils.rgb2gray(image)
            gray = True
        else:
            image = cv.imread(IMAGE_PATH)
            gray = False

def main():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

main()
