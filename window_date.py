# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'date.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Date(object):
    def setupUi(self, Date):
        Date.setObjectName("Date")
        Date.resize(400, 300)
        self.Status_label = QtWidgets.QLabel(Date)
        self.Status_label.setGeometry(QtCore.QRect(30, 10, 331, 20))
        self.Status_label.setObjectName("Status_label")
        self.Query_Date = QtWidgets.QDateEdit(Date)
        self.Query_Date.setGeometry(QtCore.QRect(30, 50, 321, 51))
        self.Query_Date.setObjectName("Query_Date")
        self.pushButton = QtWidgets.QPushButton(Date)
        self.pushButton.setGeometry(QtCore.QRect(30, 110, 151, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Date)
        self.pushButton_2.setGeometry(QtCore.QRect(203, 110, 151, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Date)
        self.lineEdit.setGeometry(QtCore.QRect(30, 200, 321, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(Date)
        self.pushButton_3.setGeometry(QtCore.QRect(203, 250, 151, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Date)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 250, 151, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.Status_label_2 = QtWidgets.QLabel(Date)
        self.Status_label_2.setGeometry(QtCore.QRect(30, 160, 331, 20))
        self.Status_label_2.setObjectName("Status_label_2")

        self.retranslateUi(Date)
        QtCore.QMetaObject.connectSlotsByName(Date)

    def retranslateUi(self, Date):
        _translate = QtCore.QCoreApplication.translate
        Date.setWindowTitle(_translate("Date", "Select Date "))
        self.Status_label.setText(_translate("Date", "Please Select The Date You Want To Enquire"))
        self.pushButton.setText(_translate("Date", "View Entries By Date"))
        self.pushButton_2.setText(_translate("Date", "Edit Entries by Date"))
        self.lineEdit.setText(_translate("Date", "Search Name"))
        self.pushButton_3.setText(_translate("Date", "Edit Entries by Name"))
        self.pushButton_4.setText(_translate("Date", "View Entries by Name"))
        self.Status_label_2.setText(_translate("Date", "Search the name of the Person"))
