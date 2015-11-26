#! /usr/bin/env python
import os
import rospy
import rospkg

from readbag import restore
from qt_gui.plugin import Plugin

from python_qt_binding.QtCore import Qt
from python_qt_binding import loadUi
from python_qt_binding.QtGui import QFileDialog, QGraphicsView, QIcon, QWidget
from PyQt4 import QtGui
from example_ui import *

class MyPlugin(Plugin):

	def pr(self, anda):
		arg = input("inserte algo")
		print arg
	def getTab(self, e):
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
		ui_file = os.path.join(rospkg.RosPack().get_path('rqt_the_teleop'), 'resource', 'MyPlugin.ui')
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

		horHeaders = []
		for n, key in enumerate(sorted(data.keys())):
			horHeaders.append(key)
			for m, item in enumerate(data[key]):
				newitem = QTableWidgetItem(item)
				self._widget.elementsTable.setItem(m, n, newitem)

		self._widget.elementsTable.setHorizontalHeaderLabels(horHeaders)
		self._widget.elementsTable.show()
		self._widget.LoadConfig.clicked[bool].connect(self.getTab)
		self._widget.pushButton_2.clicked[bool].connect(self.pr)
		self._widget.pushButton_3.clicked[bool].connect(self.pr)
		self._widget.pushButton_4.clicked[bool].connect(self.pr)
		self._widget.pushButton_5.clicked[bool].connect(self.pr)


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

