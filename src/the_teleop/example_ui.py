#! /usr/bin/env python
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
 
data = {'col1':['1','2','3'], 'col2':['4','5','6'], 'col3':['7','8','9']}
 
class MyTable(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.setmydata()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
 
    def setmydata(self):
 
        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)
 