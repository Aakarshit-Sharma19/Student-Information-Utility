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
        Dialog.resize(773, 589)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Group_StuName = QtWidgets.QGroupBox(Dialog)
        self.Group_StuName.setObjectName("Group_StuName")
        self.StuName = QtWidgets.QLineEdit(self.Group_StuName)
        self.StuName.setGeometry(QtCore.QRect(20, 30, 591, 28))
        self.StuName.setText("")
        self.StuName.setObjectName("StuName")
        self.gridLayout.addWidget(self.Group_StuName, 0, 0, 1, 3)
        self.Group_StuAddress = QtWidgets.QGroupBox(Dialog)
        self.Group_StuAddress.setObjectName("Group_StuAddress")
        self.StuAddress = QtWidgets.QLineEdit(self.Group_StuAddress)
        self.StuAddress.setGeometry(QtCore.QRect(20, 30, 591, 28))
        self.StuAddress.setText("")
        self.StuAddress.setObjectName("StuAddress")
        self.gridLayout.addWidget(self.Group_StuAddress, 1, 0, 1, 3)
        self.Group_Interest = QtWidgets.QGroupBox(Dialog)
        self.Group_Interest.setObjectName("Group_Interest")
        self.Stu_Interest = QtWidgets.QLineEdit(self.Group_Interest)
        self.Stu_Interest.setGeometry(QtCore.QRect(20, 30, 591, 28))
        self.Stu_Interest.setText("")
        self.Stu_Interest.setObjectName("Stu_Interest")
        self.gridLayout.addWidget(self.Group_Interest, 2, 0, 1, 3)
        self.Group_StuPhone = QtWidgets.QGroupBox(Dialog)
        self.Group_StuPhone.setObjectName("Group_StuPhone")
        self.StuPhone = QtWidgets.QLineEdit(self.Group_StuPhone)
        self.StuPhone.setGeometry(QtCore.QRect(20, 30, 181, 28))
        self.StuPhone.setText("")
        self.StuPhone.setObjectName("StuPhone")
        self.gridLayout.addWidget(self.Group_StuPhone, 3, 0, 1, 3)
        self.Group_Remarks = QtWidgets.QGroupBox(Dialog)
        self.Group_Remarks.setObjectName("Group_Remarks")
        self.Remarks = QtWidgets.QPlainTextEdit(self.Group_Remarks)
        self.Remarks.setGeometry(QtCore.QRect(10, 20, 601, 61))
        self.Remarks.setPlainText("")
        self.Remarks.setObjectName("Remarks")
        self.gridLayout.addWidget(self.Group_Remarks, 5, 0, 1, 3)
        self.delete_entry = QtWidgets.QPushButton(Dialog)
        self.delete_entry.setObjectName("delete_entry")
        self.gridLayout.addWidget(self.delete_entry, 6, 0, 1, 1)
        self.save_entry = QtWidgets.QPushButton(Dialog)
        self.save_entry.setObjectName("save_entry")
        self.gridLayout.addWidget(self.save_entry, 6, 1, 1, 1)
        self.cancel = QtWidgets.QPushButton(Dialog)
        self.cancel.setObjectName("cancel")
        self.gridLayout.addWidget(self.cancel, 6, 2, 1, 1)
        self.Group_StuDate = QtWidgets.QGroupBox(Dialog)
        self.Group_StuDate.setObjectName("Group_StuDate")
        self.StuDate = QtWidgets.QDateEdit(self.Group_StuDate)
        self.StuDate.setGeometry(QtCore.QRect(20, 30, 135, 30))
        self.StuDate.setObjectName("StuDate")
        self.gridLayout.addWidget(self.Group_StuDate, 4, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Group_StuName.setTitle(_translate("Dialog", "Name"))
        self.Group_StuAddress.setTitle(_translate("Dialog", "Address"))
        self.Group_Interest.setTitle(_translate("Dialog", "Area of Interest"))
        self.Group_StuPhone.setTitle(_translate("Dialog", "Phone Number"))
        self.Group_Remarks.setTitle(_translate("Dialog", "Remarks"))
        self.delete_entry.setText(_translate("Dialog", "Delete Entry"))
        self.save_entry.setText(_translate("Dialog", "Save and Exit"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.Group_StuDate.setTitle(_translate("Dialog", "Date"))
