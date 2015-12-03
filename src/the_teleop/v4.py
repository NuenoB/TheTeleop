# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changueCommand.ui'
#
# Created: Thu Dec  3 15:41:04 2015
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


class QLineEdit_keydetecter(QtGui.QLineEdit):
    def keyPressEvent(self, event):
        key = event.key()
        translate_key = str(key)

        if key in range(256):
            translate_key = str(chr(key))
        self.setText(translate_key)

        print key


class Ui_Changue_Command(object):
    def setupUi(self, Changue_Command):
        Changue_Command.setObjectName(_fromUtf8("Changue_Command"))
        Changue_Command.resize(308, 258)
        self.cancel_command = QtGui.QPushButton(Changue_Command)
        self.cancel_command.setGeometry(QtCore.QRect(40, 170, 98, 27))
        self.cancel_command.setObjectName(_fromUtf8("cancel_command"))
        self.change_command = QtGui.QPushButton(Changue_Command)
        self.change_command.setGeometry(QtCore.QRect(170, 170, 98, 27))
        self.change_command.setObjectName(_fromUtf8("change_command"))
        self.currents_commands = QtGui.QComboBox(Changue_Command)
        self.currents_commands.setGeometry(QtCore.QRect(40, 80, 101, 27))
        self.currents_commands.setObjectName(_fromUtf8("currents_commands"))
        self.new_command = QLineEdit_keydetecter(Changue_Command)
        self.new_command.setGeometry(QtCore.QRect(160, 80, 113, 27))
        self.new_command.setObjectName(_fromUtf8("new_command"))

        self.retranslateUi(Changue_Command)
        QtCore.QMetaObject.connectSlotsByName(Changue_Command)

    def retranslateUi(self, Changue_Command):
        Changue_Command.setWindowTitle(_translate("Changue_Command", "Dialog", None))
        self.cancel_command.setText(_translate("Changue_Command", "Cancel", None))
        self.change_command.setText(_translate("Changue_Command", "Change", None))

