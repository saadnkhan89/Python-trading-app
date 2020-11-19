#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from funtrd import *
from apptest1 import *
import sys


class t1(Ui_MainWindow):
    def __init__(self,window):
        self.setupUi(window)
        self.pushButton.clicked.connect(self.t2)
        self.pushButton_2.clicked.connect(self.clrt12)
    
    
    
    def t2(self):
        nm=self.lineEdit.text()
        sb=self.lineEdit_2.text()
        ef=self.lineEdit_3.text()
        tp=self.comboBox.currentText()
        sm=self.horizontalSlider.value()
        lm=self.horizontalSlider_2.value()
        x=TRADE(nm,tp,sb,ef,sm,lm)
        a=[1,2,3]
        b=[2,3,4]
        c=[10,11,12]
        d=[10,11,12]
        self.Plotwidget.plot((a,c),(b,d))
        #print(nm,tp,sb,ef,sm,lm)
        #print(fig)

    def clrt12(self):
        self.Plotwidget.clear()  
    
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui=t1(MainWindow)
MainWindow.show()
app.exec_()

