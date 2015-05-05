# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splash.ui'
#
# Created: Sun Dec  7 18:18:46 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 300)
        Dialog.setCursor(QtCore.Qt.ArrowCursor)
        Dialog.setWindowOpacity(0.8)
        Dialog.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 471, 311))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 80, 271, 101))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.progressbar = QtGui.QProgressBar(self.frame)
        self.progressbar.setGeometry(QtCore.QRect(0, 283, 451, 20))
        self.progressbar.setCursor(QtCore.Qt.WaitCursor)
        self.progressbar.setMouseTracking(False)
        self.progressbar.setProperty("value", 24)
        self.progressbar.setStyleSheet(" QProgressBar {\n"
"     border: 2px solid grey;\n"
"     border-radius: 6px;\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     background-color: #ADADAD;\n"
"     width: 4px;\n"
"     \n"
"}")
        self.progressbar.setObjectName("progressbar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Hackthis:)", None, QtGui.QApplication.UnicodeUTF8))

