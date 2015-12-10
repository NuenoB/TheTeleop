# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

board_keys= {}
board_keys[16777235] = "UP"
board_keys[16777237] = "DOWN"
board_keys[16777234] = "LEFT"
board_keys[16777236] = "RIGHT"
board_keys[32] = "SPACE"

class QLineEdit_keyDetecter(QtGui.QLineEdit):
    def keyPressEvent(self, event):
        key = event.key()
        translate_key = str(key)

        if  (key in board_keys):
        	translate_key = board_keys[key] 
        elif key in range(256):
            translate_key = str(chr(key))


        self.setText(translate_key)

class QLineEdit_keyDetecter_messegerSender(QLineEdit_keyDetecter):
    def __init__(self, parent=None):
        #print "padre de qkdms" + str(parent)
        super(QLineEdit_keyDetecter_messegerSender,self).__init__(parent)
        self.form=parent

    def keyPressEvent(self, event):
        QLineEdit_keyDetecter.keyPressEvent(self,event)
        key = event.key()
        translate_key = str(event.key())
        if key in range(256):
            translate_key = str(chr(key))
        self.form.msjsend(translate_key)

