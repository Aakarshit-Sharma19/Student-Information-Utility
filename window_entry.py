# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entry.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(926, 633)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Group_StuName = QtWidgets.QGroupBox(Dialog)
        self.Group_StuName.setObjectName("Group_StuName")
        self.StuName = QtWidgets.QLineEdit(self.Group_StuName)
        self.StuName.setGeometry(QtCore.QRect(20, 30, 861, 28))
        self.StuName.setObjectName("StuName")
        self.gridLayout.addWidget(self.Group_StuName, 0, 0, 1, 4)
        self.Group_StuAddress = QtWidgets.QGroupBox(Dialog)
        self.Group_StuAddress.setObjectName("Group_StuAddress")
        self.StuAddress = QtWidgets.QLineEdit(self.Group_StuAddress)
        self.StuAddress.setGeometry(QtCore.QRect(20, 30, 861, 28))
        self.StuAddress.setObjectName("StuAddress")
        self.gridLayout.addWidget(self.Group_StuAddress, 1, 0, 1, 4)
        self.Group_Interest = QtWidgets.QGroupBox(Dialog)
        self.Group_Interest.setObjectName("Group_Interest")
        self.Interest = QtWidgets.QLineEdit(self.Group_Interest)
        self.Interest.setGeometry(QtCore.QRect(20, 30, 861, 28))
        self.Interest.setObjectName("Interest")
        self.gridLayout.addWidget(self.Group_Interest, 2, 0, 1, 4)
        self.Group_StuPhone = QtWidgets.QGroupBox(Dialog)
        self.Group_StuPhone.setObjectName("Group_StuPhone")
        self.StuPhone = QtWidgets.QLineEdit(self.Group_StuPhone)
        self.StuPhone.setGeometry(QtCore.QRect(20, 30, 171, 28))
        self.StuPhone.setObjectName("StuPhone")
        self.gridLayout.addWidget(self.Group_StuPhone, 3, 0, 1, 4)
        self.Group_StuDate = QtWidgets.QGroupBox(Dialog)
        self.Group_StuDate.setObjectName("Group_StuDate")
        self.StuDate = QtWidgets.QDateEdit(self.Group_StuDate)
        self.StuDate.setGeometry(QtCore.QRect(20, 30, 135, 30))
        self.StuDate.setObjectName("StuDate")
        self.gridLayout.addWidget(self.Group_StuDate, 4, 0, 1, 4)
        self.Group_Remarks = QtWidgets.QGroupBox(Dialog)
        self.Group_Remarks.setObjectName("Group_Remarks")
        self.Remarks = QtWidgets.QPlainTextEdit(self.Group_Remarks)
        self.Remarks.setGeometry(QtCore.QRect(20, 30, 861, 51))
        self.Remarks.setObjectName("Remarks")
        self.gridLayout.addWidget(self.Group_Remarks, 5, 0, 1, 4)
        self.Save_Status = QtWidgets.QLabel(Dialog)
        self.Save_Status.setText("")
        self.Save_Status.setObjectName("Save_Status")
        self.gridLayout.addWidget(self.Save_Status, 8, 0, 1, 1)
        self.Save_Exit_Button = QtWidgets.QPushButton(Dialog)
        self.Save_Exit_Button.setObjectName("Save_Exit_Button")
        self.gridLayout.addWidget(self.Save_Exit_Button, 8, 2, 1, 1)
        self.Cancel_Button = QtWidgets.QPushButton(Dialog)
        self.Cancel_Button.setObjectName("Cancel_Button")
        self.gridLayout.addWidget(self.Cancel_Button, 8, 3, 1, 1)
        self.Save_New_Button = QtWidgets.QPushButton(Dialog)
        self.Save_New_Button.setObjectName("Save_New_Button")
        self.gridLayout.addWidget(self.Save_New_Button, 8, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New Entry"))
        self.Group_StuName.setTitle(_translate("Dialog", "Name"))
        self.StuName.setText(_translate("Dialog", "Type the Student\'s Name Here"))
        self.Group_StuAddress.setTitle(_translate("Dialog", "Address"))
        self.StuAddress.setText(_translate("Dialog", "Student\'s Address"))
        self.Group_Interest.setTitle(_translate("Dialog", "Area of Interest"))
        self.Interest.setText(_translate("Dialog", "In what field,  the student is interested? Eg.:- Hospitality,Hotel Management"))
        self.Group_StuPhone.setTitle(_translate("Dialog", "Phone Number"))
        self.StuPhone.setText(_translate("Dialog", "Enter Phone Number"))
        self.Group_StuDate.setTitle(_translate("Dialog", "Date"))
        self.Group_Remarks.setTitle(_translate("Dialog", "Remarks"))
        self.Remarks.setPlainText(_translate("Dialog", "Remarks or extra information pertaining to the student."))
        self.Save_Exit_Button.setText(_translate("Dialog", "Save and Exit"))
        self.Cancel_Button.setText(_translate("Dialog", "Cancel"))
        self.Save_New_Button.setText(_translate("Dialog", "Save and New Entry"))
