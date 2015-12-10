# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirm.ui'
#
# Created: Thu Dec 10 11:19:44 2015
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

class Ui_Confirm(object):
    def setupUi(self, Confirm):
        Confirm.setObjectName(_fromUtf8("Confirm"))
        Confirm.resize(308, 130)
        self.yes = QtGui.QPushButton(Confirm)
        self.yes.setGeometry(QtCore.QRect(30, 90, 98, 27))
        self.yes.setObjectName(_fromUtf8("yes"))
        self.no = QtGui.QPushButton(Confirm)
        self.no.setGeometry(QtCore.QRect(160, 90, 98, 27))
        self.no.setObjectName(_fromUtf8("no"))
        self.label = QtGui.QLabel(Confirm)
        self.label.setGeometry(QtCore.QRect(10, 20, 281, 51))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Confirm)
        QtCore.QMetaObject.connectSlotsByName(Confirm)

    def retranslateUi(self, Confirm):
        Confirm.setWindowTitle(_translate("Confirm", "Dialog", None))
        self.yes.setText(_translate("Confirm", "Yes", None))
        self.no.setText(_translate("Confirm", "No", None))

