#! /usr/bin/env python
import os
import rospy
import rospkg

from readbag import restore
from qt_gui.plugin import Plugin
from sender import sender

from python_qt_binding.QtCore import Qt
from python_qt_binding import loadUi
from python_qt_binding.QtGui import QFileDialog, QGraphicsView, QIcon, QWidget
from PyQt4 import QtGui, QtCore
from example_ui import *
from PyQt4 import QtGui
from main_ui import Ui_Form
from v2 import Ui_addbag
from v3 import Ui_AddCommandDialog
from v4 import Ui_Changue_Command
from v5 import Ui_delete_command
from confirm import Ui_Confirm
from main import *
from writebag import *

bag_path = os.path.join(rospkg.RosPack().get_path('rqt_the_teleop'), 'src/the_teleop/')

class Form1(QtGui.QWidget, Ui_Form):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        rospy.init_node('the_teleop_UI', anonymous=True)
        self.current_setting = 0
        self.current_bag = 0
        self.load_bags()
        self.get_setting()
        self.LoadConfig.clicked[bool].connect(self.get_setting)
        self.Add_Bag.clicked.connect(self.handleButton)
        self.Add_Command.clicked[bool].connect(self.AddCommandWindow)
        self.ChangeCommand.clicked[bool].connect(self.ChangeCommandWindow)
        self.Delete_Command.clicked[bool].connect(self.handle_delete_command)
        self.Delete_Bag.clicked[bool].connect(self.handle_Delete_Bag)
        print "yo mismo" + str(self)
    
    def  load_commands(self):
        self.elementsTable.clear()
        items={}
        i = 0
        cs = self.current_setting 
        for key in cs.keys():
            items[i] = QTreeWidgetItem(self.elementsTable)
            items[i].setText(0, key)
            items[i].setText(1, cs[key][topic_index])
            items[i].setText(2, str(cs[key][msg_index]))
            items[i].setText(3, cs[key][type_index])
            items[i].setText(4, str(cs[key][rate_index].to_nsec() % 100000 ))
            i=i+1

    def handle_Delete_Bag(self):
        self.window2 = form_confirm_delete_bag(self.current_bag)
        self.window2.exec_()
        if self.window2.delete==1:
            os.remove(bag_path + self.current_bag + ".bag" )
            self.load_bags()
            self.get_setting()

    def get_setting(self):
        self.current_bag = self.comboBox.currentText()
        robot_name = self.current_bag
        robot_setting = restore(bag_path + robot_name)
        self.current_setting = robot_setting
        self.load_commands()

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
        self.load_commands()


    def AddCommandWindow(self):
        self.window2 = Form3(self.current_bag, self.current_setting)
        self.window2.exec_()
        self.current_setting = self.window2.setting
        self.auto_save()

    def ChangeCommandWindow(self):
        self.window2 = Form4(self.current_bag,self.current_setting)
        self.window2.exec_()
        self.current_setting = self.window2.setting
        self.auto_save()

    def handle_delete_command(self):
        self.window2 = Form5(self.current_bag,self.current_setting)
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

    def msjsend(self, key):
        print "sending menssage" + str(key)
        self.current_setting
        if key in self.current_setting:
            val = lookup(self.current_setting,key)
            topic = val[topic_index]
            msg = val[msg_index]
            msg_type = val[type_index]
            sender(msg, topic, msg_type)
        else:
            print "No existe ese boton"

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
    def __init__(self, name_bag ,current_setting ,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.name_bag = name_bag
        self.setting = current_setting
        self.cancel_add.clicked.connect(self.handle_close_windows)
        self.correct_add.clicked.connect(self.handle_add_command)

    def handle_add_command(self):
        self.setting = agregar(self.setting, self.add_key.text(), self.add_topic.text(), self.add_msj.toPlainText(), int(self.add_rate.text()),self.add_type.text())
        self.close()

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
        ##self.load_init() load all the bananas
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

class form_confirm_delete_bag(QDialog, Ui_Confirm):
    def __init__(self, name_bag, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.name_bag = name_bag
        self.delete=0
        self.label.setText("Are you sure you want to delete this bag:\n "+ self.name_bag)
        self.yes.clicked.connect(self.handle_yes)
        self.no.clicked.connect(self.handle_no)

    def handle_yes(self):
        self.delete=1
        self.close()

    def handle_no(self):
        self.close()


if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Form1()
    window.show()
    sys.exit(app.exec_())