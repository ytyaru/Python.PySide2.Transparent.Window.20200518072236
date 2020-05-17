#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, os, numpy, PIL, csv
from PySide2 import QtCore, QtGui, QtWidgets
from PIL import Image, ImagePalette, ImageQt, ImageSequence

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setAcceptDrops(True)
        self.setWindowTitle("Transparent window")
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        palette = QtGui.QPalette(QtCore.Qt.transparent)
        self.setPalette(palette);
        self.setAutoFillBackground(True);
        self.show()
    def paintEvent(self, event):
        p = QtGui.QPainter(self)
        p.fillRect(self.rect(), QtCore.Qt.transparent);

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

