# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buddytab.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(502, 163)
        self.labelNumItems = QtWidgets.QLabel(Dialog)
        self.labelNumItems.setGeometry(QtCore.QRect(20, 20, 101, 21))
        self.labelNumItems.setObjectName("labelNumItems")
        self.labelDiscountPercentage = QtWidgets.QLabel(Dialog)
        self.labelDiscountPercentage.setGeometry(QtCore.QRect(20, 60, 101, 21))
        self.labelDiscountPercentage.setObjectName("labelDiscountPercentage")
        self.labelPriceItem = QtWidgets.QLabel(Dialog)
        self.labelPriceItem.setGeometry(QtCore.QRect(280, 20, 91, 21))
        self.labelPriceItem.setObjectName("labelPriceItem")
        self.labelResult = QtWidgets.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(20, 100, 471, 16))
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.lineQuantity = QtWidgets.QLineEdit(Dialog)
        self.lineQuantity.setGeometry(QtCore.QRect(130, 20, 113, 20))
        self.lineQuantity.setObjectName("lineQuantity")
        self.lineRate = QtWidgets.QLineEdit(Dialog)
        self.lineRate.setGeometry(QtCore.QRect(380, 20, 113, 20))
        self.lineRate.setObjectName("lineRate")
        self.lineDiscount = QtWidgets.QLineEdit(Dialog)
        self.lineDiscount.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.lineDiscount.setObjectName("lineDiscount")
        self.btnCalculate = QtWidgets.QPushButton(Dialog)
        self.btnCalculate.setGeometry(QtCore.QRect(20, 130, 471, 23))
        self.btnCalculate.setObjectName("btnCalculate")
        self.labelNumItems.setBuddy(self.lineQuantity)
        self.labelDiscountPercentage.setBuddy(self.lineDiscount)
        self.labelPriceItem.setBuddy(self.lineRate)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineQuantity, self.lineRate)
        Dialog.setTabOrder(self.lineRate, self.lineDiscount)
        Dialog.setTabOrder(self.lineDiscount, self.btnCalculate)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelNumItems.setText(_translate("Dialog", "&Number of Items"))
        self.labelDiscountPercentage.setText(_translate("Dialog", "&Discount Percentage"))
        self.labelPriceItem.setText(_translate("Dialog", "&Price Per Item"))
        self.btnCalculate.setText(_translate("Dialog", "Calculate Amount"))

