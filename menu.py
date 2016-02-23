import sys
from PyQt4 import QtGui, QtCore
import roi
import chroma
import utils
import cv2 as cv

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(250, 250, 500, 400)
        self.setWindowTitle('Computer Vision')
        self.home()
    def home(self):
        btn = QtGui.QPushButton('roi', self)
        btn.clicked.connect(self.show_roi)
        btn.resize(100, 50)
        btn.move(100, 100)

        btn = QtGui.QPushButton('chroma', self)
        btn.clicked.connect(self.show_chroma)
        btn.resize(100, 50)
        btn.move(300, 100)

        self.show()
    def show_roi(self):
        roi.play()

    def show_chroma(self):
        chroma.play()

def main():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

main()
