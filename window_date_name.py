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
        Date.resize(458, 379)
        self.gridLayout_2 = QtWidgets.QGridLayout(Date)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.date_label = QtWidgets.QLabel(Date)
        self.date_label.setObjectName("date_label")
        self.gridLayout_3.addWidget(self.date_label, 0, 0, 1, 2)
        self.query_date = QtWidgets.QDateEdit(Date)
        self.query_date.setObjectName("query_date")
        self.gridLayout_3.addWidget(self.query_date, 1, 0, 1, 2)
        self.view_bydate = QtWidgets.QPushButton(Date)
        self.view_bydate.setObjectName("view_bydate")
        self.gridLayout_3.addWidget(self.view_bydate, 2, 0, 1, 1)
        self.edit_bydate = QtWidgets.QPushButton(Date)
        self.edit_bydate.setObjectName("edit_bydate")
        self.gridLayout_3.addWidget(self.edit_bydate, 2, 1, 1, 1)
        self.name_label = QtWidgets.QLabel(Date)
        self.name_label.setObjectName("name_label")
        self.gridLayout_3.addWidget(self.name_label, 3, 0, 1, 2)
        self.query_name = QtWidgets.QLineEdit(Date)
        self.query_name.setObjectName("query_name")
        self.gridLayout_3.addWidget(self.query_name, 4, 0, 1, 2)
        self.view_byname = QtWidgets.QPushButton(Date)
        self.view_byname.setObjectName("view_byname")
        self.gridLayout_3.addWidget(self.view_byname, 5, 0, 1, 1)
        self.edit_byname = QtWidgets.QPushButton(Date)
        self.edit_byname.setObjectName("edit_byname")
        self.gridLayout_3.addWidget(self.edit_byname, 5, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Date)
        QtCore.QMetaObject.connectSlotsByName(Date)

    def retranslateUi(self, Date):
        _translate = QtCore.QCoreApplication.translate
        Date.setWindowTitle(_translate("Date", "Select Date "))
        self.date_label.setText(_translate("Date", "Please Select The Date You Want To Enquire"))
        self.view_bydate.setText(_translate("Date", "View Entries By Date"))
        self.edit_bydate.setText(_translate("Date", "Edit Entries by Date"))
        self.name_label.setText(_translate("Date", "Search the name of the Person"))
        self.query_name.setText(_translate("Date", "Search Name"))
        self.view_byname.setText(_translate("Date", "View Entries by Name"))
        self.edit_byname.setText(_translate("Date", "Edit Entries by Name"))
