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
from v1 import Ui_Form

class Form1(QtGui.QWidget, Ui_Form):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        robot_name ="/test"
        bag_path = os.path.join(rospkg.RosPack().get_path('rqt_the_teleop'), 'src/the_teleop')
        robot_setting = restore(bag_path + robot_name) 
        print robot_setting
        list_bags = self.getBags(bag_path)
        #print list_bags
        for b in list_bags:
            self._widget.comboBox.addItem(b)
        #self.button1.clicked.connect(self.handleButton)
        #self.window2 = None

    #def handleButton(self):
     #   if self.window2 is None:
      #      self.window2 = Form2(self)
       # self.window2.show()

    def getTab(self):
        arg = self._widget.comboBox.currentText ()
        print str(arg)

    def getBags(self, bag_path):
        list_bags = os.listdir(bag_path)
        list_of_bag = []
        for t in list_bags:
            if ".bag" in t:
                t = t.split('.')
                list_of_bag.append(t[0])

        return list_of_bag

#class Form2(QtGui.QWidget, Ui_Form2):
 #   def __init__(self, parent=None):
  #      QtGui.QWidget.__init__(self, parent)
   #     self.setupUi(self)

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Form1()
    window.show()
    sys.exit(app.exec_())