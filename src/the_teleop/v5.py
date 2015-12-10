# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete.ui'
#
# Created: Thu Dec 10 11:19:52 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_delete_command(object):
    def setupUi(self, delete_command):
        delete_command.setObjectName(_fromUtf8("delete_command"))
        delete_command.resize(185, 194)
        self.currents_commands = QtGui.QComboBox(delete_command)
        self.currents_commands.setGeometry(QtCore.QRect(50, 50, 78, 27))
        self.currents_commands.setObjectName(_fromUtf8("currents_commands"))
        self.delete_boton = QtGui.QPushButton(delete_command)
        self.delete_boton.setGeometry(QtCore.QRect(40, 90, 98, 27))
        self.delete_boton.setObjectName(_fromUtf8("delete_boton"))
        self.close_windows = QtGui.QPushButton(delete_command)
        self.close_windows.setGeometry(QtCore.QRect(40, 130, 98, 27))
        self.close_windows.setObjectName(_fromUtf8("close_windows"))
        self.label = QtGui.QLabel(delete_command)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 17))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(delete_command)
        QtCore.QMetaObject.connectSlotsByName(delete_command)

    def retranslateUi(self, delete_command):
        delete_command.setWindowTitle(_translate("delete_command", "Dialog", None))
        self.delete_boton.setText(_translate("delete_command", "Delete", None))
        self.close_windows.setText(_translate("delete_command", "Exit", None))
        self.label.setText(_translate("delete_command", "Select to delete", None))

