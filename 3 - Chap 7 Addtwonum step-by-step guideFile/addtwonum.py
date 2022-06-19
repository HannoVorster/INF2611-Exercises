# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addtwonum.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(262, 165)
        self.labelFirstNumber = QtWidgets.QLabel(Dialog)
        self.labelFirstNumber.setGeometry(QtCore.QRect(20, 10, 111, 21))
        self.labelFirstNumber.setObjectName("labelFirstNumber")
        self.labelAddition = QtWidgets.QLabel(Dialog)
        self.labelAddition.setGeometry(QtCore.QRect(130, 100, 111, 16))
        self.labelAddition.setText("")
        self.labelAddition.setObjectName("labelAddition")
        self.labelSecondNumber = QtWidgets.QLabel(Dialog)
        self.labelSecondNumber.setGeometry(QtCore.QRect(20, 60, 111, 20))
        self.labelSecondNumber.setObjectName("labelSecondNumber")
        self.AddButton = QtWidgets.QPushButton(Dialog)
        self.AddButton.setGeometry(QtCore.QRect(20, 130, 221, 23))
        self.AddButton.setObjectName("AddButton")
        self.lineFirstNumber = QtWidgets.QLineEdit(Dialog)
        self.lineFirstNumber.setGeometry(QtCore.QRect(130, 10, 113, 20))
        self.lineFirstNumber.setObjectName("lineFirstNumber")
        self.lineSecondNumber = QtWidgets.QLineEdit(Dialog)
        self.lineSecondNumber.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.lineSecondNumber.setObjectName("lineSecondNumber")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelFirstNumber.setText(_translate("Dialog", "Enter First Number"))
        self.labelSecondNumber.setText(_translate("Dialog", "Enter Second Number"))
        self.AddButton.setText(_translate("Dialog", "Add"))

