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
        self.label_2 = QtWidgets.QLabel(self.Group_StuName)
        self.label_2.setGeometry(QtCore.QRect(10, 27, 371, 21))
        self.label_2.setObjectName("label_2")
        self.Group_StuAddress = QtWidgets.QGroupBox(Dialog)
        self.Group_StuAddress.setGeometry(QtCore.QRect(10, 80, 621, 61))
        self.Group_StuAddress.setObjectName("Group_StuAddress")
        self.label_3 = QtWidgets.QLabel(self.Group_StuAddress)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 571, 18))
        self.label_3.setObjectName("label_3")
        self.Group_Interest = QtWidgets.QGroupBox(Dialog)
        self.Group_Interest.setGeometry(QtCore.QRect(10, 150, 621, 61))
        self.Group_Interest.setObjectName("Group_Interest")
        self.label_4 = QtWidgets.QLabel(self.Group_Interest)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 491, 18))
        self.label_4.setObjectName("label_4")
        self.Group_StuPhone = QtWidgets.QGroupBox(Dialog)
        self.Group_StuPhone.setGeometry(QtCore.QRect(10, 220, 621, 61))
        self.Group_StuPhone.setObjectName("Group_StuPhone")
        self.label_5 = QtWidgets.QLabel(self.Group_StuPhone)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 161, 18))
        self.label_5.setObjectName("label_5")
        self.Group_StuName_5 = QtWidgets.QGroupBox(Dialog)
        self.Group_StuName_5.setGeometry(QtCore.QRect(10, 290, 621, 61))
        self.Group_StuName_5.setObjectName("Group_StuName_5")
        self.label = QtWidgets.QLabel(self.Group_StuName_5)
        self.label.setGeometry(QtCore.QRect(20, 30, 181, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.Group_StuName_5)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 211, 18))
        self.label_6.setObjectName("label_6")
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
        self.label_2.setText(_translate("Dialog", "Name"))
        self.Group_StuAddress.setTitle(_translate("Dialog", "Address"))
        self.label_3.setText(_translate("Dialog", "Address"))
        self.Group_Interest.setTitle(_translate("Dialog", "Area of Interest"))
        self.label_4.setText(_translate("Dialog", "Interest"))
        self.Group_StuPhone.setTitle(_translate("Dialog", "Phone Number"))
        self.label_5.setText(_translate("Dialog", "Phone"))
        self.Group_StuName_5.setTitle(_translate("Dialog", "Date"))
        self.label_6.setText(_translate("Dialog", "TextLabel"))
        self.pushButton_2.setText(_translate("Dialog", "Save and Exit"))
        self.pushButton_3.setText(_translate("Dialog", "Cancel"))
        self.groupBox.setTitle(_translate("Dialog", "Remarks"))
