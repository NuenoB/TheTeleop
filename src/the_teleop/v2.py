# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddBag.ui'
#
# Created: Thu Dec 10 11:24:37 2015
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

class Ui_addbag(object):
    def setupUi(self, addbag):
        addbag.setObjectName(_fromUtf8("addbag"))
        addbag.resize(231, 177)
        self.label = QtGui.QLabel(addbag)
        self.label.setGeometry(QtCore.QRect(50, 20, 121, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(addbag)
        self.lineEdit.setGeometry(QtCore.QRect(50, 50, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.add_bag_cancel = QtGui.QPushButton(addbag)
        self.add_bag_cancel.setGeometry(QtCore.QRect(10, 110, 98, 27))
        self.add_bag_cancel.setObjectName(_fromUtf8("add_bag_cancel"))
        self.create_new_bag = QtGui.QPushButton(addbag)
        self.create_new_bag.setGeometry(QtCore.QRect(120, 110, 98, 27))
        self.create_new_bag.setObjectName(_fromUtf8("create_new_bag"))

        self.retranslateUi(addbag)
        QtCore.QMetaObject.connectSlotsByName(addbag)

    def retranslateUi(self, addbag):
        addbag.setWindowTitle(_translate("addbag", "Dialog", None))
        self.label.setText(_translate("addbag", "Insert New Robot", None))
        self.add_bag_cancel.setText(_translate("addbag", "Cancel", None))
        self.create_new_bag.setText(_translate("addbag", "Create", None))

