# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splash.ui'
#
# Created: Mon May  4 10:52:07 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(470, 307)
        Dialog.setCursor(QtCore.Qt.ArrowCursor)
        Dialog.setWindowOpacity(1.0)
        Dialog.setStyleSheet("border:0;")
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 471, 311))
        self.frame.setStyleSheet("background-color: rgb(0,0,0);")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 80, 291, 101))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.progressbar = QtGui.QProgressBar(self.frame)
        self.progressbar.setGeometry(QtCore.QRect(10, 280, 451, 16))
        self.progressbar.setCursor(QtCore.Qt.WaitCursor)
        self.progressbar.setMouseTracking(False)
        self.progressbar.setStyleSheet(" QProgressBar {\n"
"     border: 2px solid grey;\n"
"     border-radius: 6px;\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     background-color: #FFFFFF;\n"
"     width: 4px;\n"
"     \n"
"}")
        self.progressbar.setProperty("value", 24)
        self.progressbar.setObjectName("progressbar")
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 256, 71, 21))
        self.label_2.setStyleSheet("color: rgb(250, 250, 250);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 151, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "HackStack", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Loading...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>Copy right &amp;copy; 2015</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

