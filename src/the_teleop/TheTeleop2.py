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
from v2 import Ui_addbag
from v3 import Ui_AddCommandDialog
from main import *
from writebag import *

bag_path = os.path.join(rospkg.RosPack().get_path('rqt_the_teleop'), 'src/the_teleop')

class Form1(QtGui.QWidget, Ui_Form):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.load_bags()
        self.LoadConfig.clicked[bool].connect(self.getTab)
        self.Add_Bag.clicked.connect(self.handleButton)
        self.Add_Command.clicked[bool].connect(self.AddCommandWindow)



    def load_bags(self):
        robot_name ="/test"
        bag_path = os.path.join(rospkg.RosPack().get_path('rqt_the_teleop'), 'src/the_teleop')
        robot_setting = restore(bag_path + robot_name) 
        print robot_setting
        list_bags = self.getBags(bag_path)
        self.comboBox.clear()
        for b in list_bags:
            self.comboBox.addItem(b)

    def handleButton(self):
        self.window2 = Form2()
        self.window2.exec_()
        self.load_bags()


    def AddCommandWindow(self):
        self.window2 = Form3(self.comboBox.currentText())
        self.window2.exec_()

    def getTab(self):
        arg = self.comboBox.currentText()
        print str(arg)

    def getBags(self, bag_path):
        list_bags = os.listdir(bag_path)
        list_of_bag = []
        for t in list_bags:
            if ".bag" in t:
                t = t.split('.')
                list_of_bag.append(t[0])
        return list_of_bag


class Form2(QDialog, Ui_addbag):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.create_new_bag.clicked.connect(self.handle_create)
        self.add_bag_cancel.clicked.connect(self.handle_close_windows)

    def handle_create(self):

        name = "/home/robotica/catkin_ws/src/rqt_the_teleop/src/the_teleop/" + self.lineEdit.text()
        emptyd = {} 
        store(emptyd ,name)
        print name

        self.close()


    def handle_close_windows(self):
        self.close()

class Form3(QDialog, Ui_AddCommandDialog):
    def __init__(self, name_bag ,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.name_bag = name_bag
        self.cancel_add.clicked.connect(self.handle_close_windows)
        self.correct_add.clicked.connect(self.handle_add_command)

    def handle_add_command(self):
        dict1 = {}
        dict1 = agregar(dict1, self.add_key.text(), self.add_topic.text(), self.add_msj.text(), int(self.add_rate.text()),self.add_type.text())
        print dict1
        print self.name_bag
        #writebag()

    def handle_close_windows(self):
        self.close()


if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Form1()
    window.show()
    sys.exit(app.exec_())