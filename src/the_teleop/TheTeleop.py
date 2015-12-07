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

class MyPlugin(Plugin):

	def pr(self, anda):
		arg = input("inserte algo")
		print arg
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

	def newWindow(self,)

	def __init__(self, context):
		super(MyPlugin, self).__init__(context)
		# Give QObjects reasonable names
		self.setObjectName('MyPlugin')
		# Process standalone plugin command-line arguments
		from argparse import ArgumentParser
		parser = ArgumentParser()
		# Add argument(s) to the parser.
		parser.add_argument("-q", "--quiet", action="store_true", dest="quiet", help="Put plugin in silent mode")
		args, unknowns = parser.parse_known_args(context.argv())
		if not args.quiet:
			print 'arguments: ', args
			print 'unknowns: ', unknowns

		# Create QWidget
		#print "i am alive"
		self._widget = QWidget()
		# Get path to UI file which should be in the "resource" folder of this package
		ui_file = os.path.join(rospkg.RosPack().get_path('rqt_the_teleop'), 'resource', 'MyPlugin.ui')#! /usr/bin/env python
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


if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Form1()
    window.show()
    sys.exit(app.exec_())
		# Extend the widget with all attributes and children from UI file
		loadUi(ui_file, self._widget)
		# Give QObjects reasonable names
		self._widget.setObjectName('MyPluginUi')
		# Show _widget.windowTitle on left-top of each plugin (when 
		# it's set in _widget). This is useful when you open multiple 
		# plugins at once. Also if you open multiple instances of your 
		# plugin at once, these lines add number to make it easy to 
		# tell from pane to pane.
		if context.serial_number() > 1:
			self._widget.setWindowTitle(self._widget.windowTitle() + (' (%d)' % context.serial_number()))
		# Add widget to the user interface
		context.add_widget(self._widget)
		
		#test

		        #tree_widget ROBOT
		self._widget.elementsTable.setEditTriggers(self._widget.elementsTable.NoEditTriggers)

		header_robot = self._widget.elementsTable.header()
		header_robot.setResizeMode(QHeaderView.ResizeToContents) 
		header_robot.setContextMenuPolicy(Qt.CustomContextMenu)


		#rospy.init_node('The_Teleop')
		print "welcome to teleop"
		#robot_name = str(input("set robot"))
		robot_name ="/test"
		bag_path = os.path.join(rospkg.RosPack().get_path('rqt_the_teleop'), 'src/the_teleop')
		robot_setting = restore(bag_path + robot_name) 
		print robot_setting
		list_bags = self.getBags(bag_path)
		#print list_bags

		for b in list_bags:
			self._widget.comboBox.addItem(b)

		# horHeaders = []
		# for n, key in enumerate(sorted(data.keys())):
		# 	horHeaders.append(key)
		# 	for m, item in enumerate(data[key]):
		# 		newitem = QTableWidgetItem(item)
		# 		self._widget.elementsTable.setItem(m, n, newitem)

		# self._widget.elementsTable.setHorizontalHeaderLabels(horHeaders)
		# self._widget.elementsTable.show()
 
		self._widget.LoadConfig.clicked[bool].connect(self.getTab)
		self._widget.Add_Bag.clicked[bool].connect(self.pr)

	def shutdown_plugin(self):
	    # TODO unregister all publishers here
		pass

	def save_settings(self, plugin_settings, instance_settings):
	    # TODO save intrinsic configuration, usually using:
	    # instance_settings.set_value(k, v)
		pass

	def restore_settings(self, plugin_settings, instance_settings):
	    # TODO restore intrinsic configuration, usually using:
	    # v = instance_settings.value(k)
		pass

	#def trigger_configuration(self):
	    # Comment in to signal that the plugin has a way to configure
	    # This will enable a setting button (gear icon) in each dock widget title bar
	    # Usually used to open a modal configuration dialog

