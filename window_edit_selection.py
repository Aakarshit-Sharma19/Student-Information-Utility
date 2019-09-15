# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit.ui'
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
        self.StuName = QtWidgets.QLineEdit(self.Group_StuName)
        self.StuName.setGeometry(QtCore.QRect(20, 30, 541, 28))
        self.StuName.setText("")
        self.StuName.setObjectName("StuName")
        self.Group_StuAddress = QtWidgets.QGroupBox(Dialog)
        self.Group_StuAddress.setGeometry(QtCore.QRect(10, 80, 621, 61))
        self.Group_StuAddress.setObjectName("Group_StuAddress")
        self.StuAddress = QtWidgets.QLineEdit(self.Group_StuAddress)
        self.StuAddress.setGeometry(QtCore.QRect(20, 30, 591, 28))
        self.StuAddress.setText("")
        self.StuAddress.setObjectName("StuAddress")
        self.Group_Interest = QtWidgets.QGroupBox(Dialog)
        self.Group_Interest.setGeometry(QtCore.QRect(10, 150, 621, 61))
        self.Group_Interest.setObjectName("Group_Interest")
        self.Interest = QtWidgets.QLineEdit(self.Group_Interest)
        self.Interest.setGeometry(QtCore.QRect(20, 30, 591, 28))
        self.Interest.setText("")
        self.Interest.setObjectName("Interest")
        self.Group_StuPhone = QtWidgets.QGroupBox(Dialog)
        self.Group_StuPhone.setGeometry(QtCore.QRect(10, 220, 621, 61))
        self.Group_StuPhone.setObjectName("Group_StuPhone")
        self.Stu_Phone = QtWidgets.QLineEdit(self.Group_StuPhone)
        self.Stu_Phone.setGeometry(QtCore.QRect(20, 30, 171, 28))
        self.Stu_Phone.setText("")
        self.Stu_Phone.setObjectName("Stu_Phone")
        self.Group_StuName_5 = QtWidgets.QGroupBox(Dialog)
        self.Group_StuName_5.setGeometry(QtCore.QRect(10, 290, 621, 61))
        self.Group_StuName_5.setObjectName("Group_StuName_5")
        self.label = QtWidgets.QLabel(self.Group_StuName_5)
        self.label.setGeometry(QtCore.QRect(20, 30, 181, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 530, 91, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 530, 84, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 370, 621, 131))
        self.groupBox.setObjectName("groupBox")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 20, 591, 101))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Group_StuName.setTitle(_translate("Dialog", "Name"))
        self.Group_StuAddress.setTitle(_translate("Dialog", "Address"))
        self.Group_Interest.setTitle(_translate("Dialog", "Area of Interest"))
        self.Group_StuPhone.setTitle(_translate("Dialog", "Phone Number"))
        self.Group_StuName_5.setTitle(_translate("Dialog", "Date"))
        self.pushButton_2.setText(_translate("Dialog", "Save and Exit"))
        self.pushButton_3.setText(_translate("Dialog", "Cancel"))
        self.groupBox.setTitle(_translate("Dialog", "Remarks"))
