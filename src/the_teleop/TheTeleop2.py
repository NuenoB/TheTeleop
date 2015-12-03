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
from v4 import Ui_Changue_Command
from v5 import Ui_delete_command
from main import *
from writebag import *

bag_path = os.path.join(rospkg.RosPack().get_path('rqt_the_teleop'), 'src/the_teleop/')

class Form1(QtGui.QWidget, Ui_Form):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.current_setting = 0
        self.current_bag = 0
        self.load_bags()
        self.get_setting()
        self.LoadConfig.clicked[bool].connect(self.get_setting)
        self.Add_Bag.clicked.connect(self.handleButton)
        self.Add_Command.clicked[bool].connect(self.AddCommandWindow)
        self.ChangeCommand.clicked[bool].connect(self.ChangeCommandWindow)
        self.Delete_Command.clicked[bool].connect(self.handle_delete_command)
    
    def get_setting(self):
        self.current_bag = self.comboBox.currentText()
        robot_name = self.current_bag
        robot_setting = restore(bag_path + robot_name)
        self.current_setting = robot_setting 

    def load_bags(self):
        list_bags = self.getBags(bag_path)
        self.comboBox.clear()
        for b in list_bags:
            self.comboBox.addItem(b)

    def handleButton(self):
        self.window2 = Form2()
        self.window2.exec_()
        self.load_bags()

    def auto_save(self):
        store(self.current_setting, bag_path + self.current_bag)


    def AddCommandWindow(self):
        self.window2 = Form3(self.comboBox.currentText())
        self.window2.exec_()
        self.auto_save()

    def ChangeCommandWindow(self):
        self.window2 = Form4(self.comboBox.currentText(),self.current_setting)
        self.window2.exec_()
        self.current_setting = self.window2.setting
        self.auto_save()

    def handle_delete_command(self):
        self.window2 = Form5(self.comboBox.currentText(),self.current_setting)
        self.window2.exec_()
        self.current_setting = self.window2.setting
        self.auto_save()

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
        dict1 = agregar(dict1, self.add_key.text(), self.add_topic.text(), self.add_msj.toPlainText(), int(self.add_rate.text()),self.add_type.text())
        print dict1
        print self.name_bag
        #writebag()

    def handle_close_windows(self):
        self.close()

class Form4(QDialog, Ui_Changue_Command):
    

    def __init__(self,name_bag,setting,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setting=0
        self.setupUi(self)
        self.name_bag = name_bag
        self.setting = setting
        self.load_init()
        ##self.load_init()
        self.cancel_command.clicked.connect(self.handle_close_windows)
        self.change_command.clicked.connect(self.handle_change_command)

    def handle_close_windows(self):
        self.close()


    def load_init(self):
        self.currents_commands.clear()
        for b in self.setting.keys():
            self.currents_commands.addItem(b)

    def handle_change_command(self):
        old_key = self.currents_commands.currentText()
        if (self.setting.has_key(old_key)):
            new_key = self.new_command.text()
            #look for
            element = self.setting[old_key]
            del self.setting[old_key]
            self.setting[new_key] = element
            print "key changed successfully"
        else:
            print "key undefined"
        self.close()


class Form5(QDialog, Ui_delete_command):
    def __init__(self,name_bag,setting,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setting=setting
        self.name_bag=name_bag
        self.load_init()
        self.delete_boton.clicked.connect(self.handle_delete_boton)
        self.close_windows.clicked.connect(self.handle_close_windows)
    
    def load_init(self):
        self.currents_commands.clear()
        for b in self.setting.keys():
            self.currents_commands.addItem(b)

    def handle_delete_boton(self):
        to_delete = self.currents_commands.currentText()
        del self.setting[to_delete]
        self.load_init()

    def handle_close_windows(self):
        self.close()


if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Form1()
    window.show()
    sys.exit(app.exec_())