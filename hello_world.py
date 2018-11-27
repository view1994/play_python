# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello_world.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(mainWindow)
        self.buttonBox.setGeometry(QtCore.QRect(30, 220, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.push_me = QtWidgets.QPushButton(mainWindow)
        self.push_me.setGeometry(QtCore.QRect(110, 10, 181, 51))
        self.push_me.setObjectName("push_me")
        self.layout = QtWidgets.QLabel(mainWindow)
        self.layout.setGeometry(QtCore.QRect(90, 70, 231, 151))
        self.layout.setLineWidth(2)
        self.layout.setTextFormat(QtCore.Qt.PlainText)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.setObjectName("layout")

        self.retranslateUi(mainWindow)
        self.buttonBox.accepted.connect(mainWindow.accept)
        self.buttonBox.rejected.connect(mainWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "mainWindow"))
        self.push_me.setText(_translate("mainWindow", "Push Me"))
        self.layout.setText(_translate("mainWindow", "hello world~~"))

