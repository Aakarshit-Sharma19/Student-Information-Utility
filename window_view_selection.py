# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(639, 557)
        self.Group_StuName = QtWidgets.QGroupBox(Dialog)
        self.Group_StuName.setGeometry(QtCore.QRect(10, 10, 621, 61))
        self.Group_StuName.setObjectName("Group_StuName")
        self.StuName = QtWidgets.QLabel(self.Group_StuName)
        self.StuName.setGeometry(QtCore.QRect(10, 27, 371, 21))
        self.StuName.setObjectName("StuName")
        self.Group_StuAddress = QtWidgets.QGroupBox(Dialog)
        self.Group_StuAddress.setGeometry(QtCore.QRect(10, 80, 621, 61))
        self.Group_StuAddress.setObjectName("Group_StuAddress")
        self.StuAddress = QtWidgets.QLabel(self.Group_StuAddress)
        self.StuAddress.setGeometry(QtCore.QRect(10, 30, 571, 18))
        self.StuAddress.setObjectName("StuAddress")
        self.Group_Interest = QtWidgets.QGroupBox(Dialog)
        self.Group_Interest.setGeometry(QtCore.QRect(10, 150, 621, 61))
        self.Group_Interest.setObjectName("Group_Interest")
        self.Interest = QtWidgets.QLabel(self.Group_Interest)
        self.Interest.setGeometry(QtCore.QRect(10, 30, 491, 18))
        self.Interest.setObjectName("Interest")
        self.Group_StuPhone = QtWidgets.QGroupBox(Dialog)
        self.Group_StuPhone.setGeometry(QtCore.QRect(10, 220, 621, 61))
        self.Group_StuPhone.setObjectName("Group_StuPhone")
        self.StuPhone = QtWidgets.QLabel(self.Group_StuPhone)
        self.StuPhone.setGeometry(QtCore.QRect(10, 30, 161, 18))
        self.StuPhone.setObjectName("StuPhone")
        self.Grup_StuDate = QtWidgets.QGroupBox(Dialog)
        self.Grup_StuDate.setGeometry(QtCore.QRect(10, 290, 621, 61))
        self.Grup_StuDate.setObjectName("Grup_StuDate")
        self.StuDate = QtWidgets.QLabel(self.Grup_StuDate)
        self.StuDate.setGeometry(QtCore.QRect(10, 30, 211, 18))
        self.StuDate.setObjectName("StuDate")
        self.OK_Button = QtWidgets.QPushButton(Dialog)
        self.OK_Button.setGeometry(QtCore.QRect(520, 520, 91, 24))
        self.OK_Button.setObjectName("OK_Button")
        self.Group_Remarks = QtWidgets.QGroupBox(Dialog)
        self.Group_Remarks.setGeometry(QtCore.QRect(10, 370, 621, 131))
        self.Group_Remarks.setObjectName("Group_Remarks")
        self.Remarks = QtWidgets.QPlainTextEdit(self.Group_Remarks)
        self.Remarks.setGeometry(QtCore.QRect(20, 20, 591, 101))
        self.Remarks.setPlainText("")
        self.Remarks.setObjectName("Remarks")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Group_StuName.setTitle(_translate("Dialog", "Name"))
        self.StuName.setText(_translate("Dialog", "Name"))
        self.Group_StuAddress.setTitle(_translate("Dialog", "Address"))
        self.StuAddress.setText(_translate("Dialog", "Address"))
        self.Group_Interest.setTitle(_translate("Dialog", "Area of Interest"))
        self.Interest.setText(_translate("Dialog", "Interest"))
        self.Group_StuPhone.setTitle(_translate("Dialog", "Phone Number"))
        self.StuPhone.setText(_translate("Dialog", "Phone"))
        self.Grup_StuDate.setTitle(_translate("Dialog", "Date"))
        self.StuDate.setText(_translate("Dialog", "Date"))
        self.OK_Button.setText(_translate("Dialog", "Ok"))
        self.Group_Remarks.setTitle(_translate("Dialog", "Remarks"))
