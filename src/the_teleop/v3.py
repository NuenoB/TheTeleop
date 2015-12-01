# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddCommand.ui'
#
# Created: Tue Dec  1 15:57:47 2015
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

class Ui_AddCommandDialog(object):
    def setupUi(self, AddCommandDialog):
        AddCommandDialog.setObjectName(_fromUtf8("AddCommandDialog"))
        AddCommandDialog.resize(361, 364)
        self.correct_add = QtGui.QPushButton(AddCommandDialog)
        self.correct_add.setGeometry(QtCore.QRect(200, 270, 98, 27))
        self.correct_add.setObjectName(_fromUtf8("correct_add"))
        self.cancel_add = QtGui.QPushButton(AddCommandDialog)
        self.cancel_add.setGeometry(QtCore.QRect(50, 270, 98, 27))
        self.cancel_add.setObjectName(_fromUtf8("cancel_add"))
        self.add_key = QtGui.QLineEdit(AddCommandDialog)
        self.add_key.setGeometry(QtCore.QRect(140, 60, 113, 27))
        self.add_key.setObjectName(_fromUtf8("add_key"))
        self.add_topic = QtGui.QLineEdit(AddCommandDialog)
        self.add_topic.setGeometry(QtCore.QRect(140, 90, 113, 27))
        self.add_topic.setObjectName(_fromUtf8("add_topic"))
        self.add_msj = QtGui.QLineEdit(AddCommandDialog)
        self.add_msj.setGeometry(QtCore.QRect(140, 120, 113, 27))
        self.add_msj.setObjectName(_fromUtf8("add_msj"))
        self.add_type = QtGui.QLineEdit(AddCommandDialog)
        self.add_type.setGeometry(QtCore.QRect(140, 150, 113, 27))
        self.add_type.setObjectName(_fromUtf8("add_type"))
        self.add_rate = QtGui.QLineEdit(AddCommandDialog)
        self.add_rate.setGeometry(QtCore.QRect(140, 180, 113, 27))
        self.add_rate.setObjectName(_fromUtf8("add_rate"))
        self.label = QtGui.QLabel(AddCommandDialog)
        self.label.setGeometry(QtCore.QRect(40, 60, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(AddCommandDialog)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(AddCommandDialog)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(AddCommandDialog)
        self.label_4.setGeometry(QtCore.QRect(40, 190, 66, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(AddCommandDialog)
        self.label_5.setGeometry(QtCore.QRect(40, 160, 66, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(AddCommandDialog)
        QtCore.QMetaObject.connectSlotsByName(AddCommandDialog)

    def retranslateUi(self, AddCommandDialog):
        AddCommandDialog.setWindowTitle(_translate("AddCommandDialog", "Dialog", None))
        self.correct_add.setText(_translate("AddCommandDialog", "Add", None))
        self.cancel_add.setText(_translate("AddCommandDialog", "Cancel", None))
        self.label.setText(_translate("AddCommandDialog", "key", None))
        self.label_2.setText(_translate("AddCommandDialog", "topic", None))
        self.label_3.setText(_translate("AddCommandDialog", "msj", None))
        self.label_4.setText(_translate("AddCommandDialog", "rate", None))
        self.label_5.setText(_translate("AddCommandDialog", "type", None))

