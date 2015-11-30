# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyPlugin.ui'
#
# Created: Mon Nov 30 09:22:43 2015
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(540, 527)
        self.ChangeCommand = QtGui.QPushButton(Form)
        self.ChangeCommand.setGeometry(QtCore.QRect(370, 180, 131, 27))
        self.ChangeCommand.setObjectName(_fromUtf8("ChangeCommand"))
        self.Add_Command = QtGui.QPushButton(Form)
        self.Add_Command.setGeometry(QtCore.QRect(40, 180, 131, 27))
        self.Add_Command.setObjectName(_fromUtf8("Add_Command"))
        self.Delete_Command = QtGui.QPushButton(Form)
        self.Delete_Command.setGeometry(QtCore.QRect(210, 180, 131, 27))
        self.Delete_Command.setObjectName(_fromUtf8("Delete_Command"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(160, 40, 91, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.Add_Bag = QtGui.QPushButton(Form)
        self.Add_Bag.setGeometry(QtCore.QRect(140, 110, 98, 27))
        self.Add_Bag.setObjectName(_fromUtf8("Add_Bag"))
        self.Delete_Bag = QtGui.QPushButton(Form)
        self.Delete_Bag.setGeometry(QtCore.QRect(310, 110, 98, 27))
        self.Delete_Bag.setObjectName(_fromUtf8("Delete_Bag"))
        self.LoadConfig = QtGui.QPushButton(Form)
        self.LoadConfig.setGeometry(QtCore.QRect(280, 40, 98, 27))
        self.LoadConfig.setObjectName(_fromUtf8("LoadConfig"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 20, 101, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.elementsTable = QtGui.QTreeWidget(Form)
        self.elementsTable.setGeometry(QtCore.QRect(140, 260, 256, 192))
        self.elementsTable.setObjectName(_fromUtf8("elementsTable"))
        item_0 = QtGui.QTreeWidgetItem(self.elementsTable)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.ChangeCommand.setText(_translate("Form", "Change Command", None))
        self.Add_Command.setText(_translate("Form", "Add Command", None))
        self.Delete_Command.setText(_translate("Form", "Delete Command", None))
        self.Add_Bag.setText(_translate("Form", "Add Bag", None))
        self.Delete_Bag.setText(_translate("Form", "Delete Bag", None))
        self.LoadConfig.setText(_translate("Form", "Load Robot", None))
        self.label.setText(_translate("Form", "Current Robot", None))
        self.elementsTable.headerItem().setText(0, _translate("Form", "1", None))
        self.elementsTable.headerItem().setText(1, _translate("Form", "2", None))
        __sortingEnabled = self.elementsTable.isSortingEnabled()
        self.elementsTable.setSortingEnabled(False)
        self.elementsTable.topLevelItem(0).setText(0, _translate("Form", "asdasd", None))
        self.elementsTable.topLevelItem(0).setText(1, _translate("Form", "asdasdasd", None))
        self.elementsTable.setSortingEnabled(__sortingEnabled)

