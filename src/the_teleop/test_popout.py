#! /usr/bin/env python
import os
import rospy
import rospkg

from readbag import restore
from qt_gui.plugin import Plugin

from python_qt_binding.QtCore import Qt
from python_qt_binding import loadUi
from python_qt_binding.QtGui import QFileDialog, QGraphicsView, QIcon, QWidget
from PyQt4 import QtGui, QtCore
from example_ui import *
from PyQt4 import QtGui
from v2 import Ui_addbag

class Form1(QtGui.QWidget, Ui_addbag):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.handleButton)
        self.window2 = None

    def handleButton(self):
        if self.window2 is None:
            self.window2 = Form1(self)
        self.window2.show()
        self.hide()



def pop():

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Form1()
    window.show()
    sys.exit(app.exec_())