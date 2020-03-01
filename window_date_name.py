# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/aakarshit/Desktop/Student-Information-Utility/UI Files/datename.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Date(object):
    def setupUi(self, Date):
        Date.setObjectName("Date")
        Date.resize(786, 494)
        self.gridLayout = QtWidgets.QGridLayout(Date)
        self.gridLayout.setObjectName("gridLayout")
        self.date_label = QtWidgets.QLabel(Date)
        self.date_label.setObjectName("date_label")
        self.gridLayout.addWidget(self.date_label, 0, 0, 1, 2)
        self.query_date = QtWidgets.QDateEdit(Date)
        self.query_date.setObjectName("query_date")
        self.gridLayout.addWidget(self.query_date, 1, 0, 1, 2)
        self.view_bydate = QtWidgets.QPushButton(Date)
        self.view_bydate.setMinimumSize(QtCore.QSize(120, 70))
        self.view_bydate.setObjectName("view_bydate")
        self.gridLayout.addWidget(self.view_bydate, 2, 0, 1, 1)
        self.edit_bydate = QtWidgets.QPushButton(Date)
        self.edit_bydate.setMinimumSize(QtCore.QSize(120, 70))
        self.edit_bydate.setObjectName("edit_bydate")
        self.gridLayout.addWidget(self.edit_bydate, 2, 1, 1, 1)
        self.name_label = QtWidgets.QLabel(Date)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 3, 0, 1, 2)
        self.query_name = QtWidgets.QLineEdit(Date)
        self.query_name.setObjectName("query_name")
        self.gridLayout.addWidget(self.query_name, 4, 0, 1, 2)
        self.view_byname = QtWidgets.QPushButton(Date)
        self.view_byname.setMinimumSize(QtCore.QSize(120, 70))
        self.view_byname.setObjectName("view_byname")
        self.gridLayout.addWidget(self.view_byname, 5, 0, 1, 1)
        self.edit_byname = QtWidgets.QPushButton(Date)
        self.edit_byname.setMinimumSize(QtCore.QSize(120, 70))
        self.edit_byname.setObjectName("edit_byname")
        self.gridLayout.addWidget(self.edit_byname, 5, 1, 1, 1)
        self.View_All_Button = QtWidgets.QPushButton(Date)
        self.View_All_Button.setMinimumSize(QtCore.QSize(120, 70))
        self.View_All_Button.setObjectName("View_All_Button")
        self.gridLayout.addWidget(self.View_All_Button, 6, 0, 1, 1)
        self.Close_Button = QtWidgets.QPushButton(Date)
        self.Close_Button.setMinimumSize(QtCore.QSize(120, 70))
        self.Close_Button.setObjectName("Close_Button")
        self.gridLayout.addWidget(self.Close_Button, 6, 1, 1, 1)

        self.retranslateUi(Date)
        QtCore.QMetaObject.connectSlotsByName(Date)

    def retranslateUi(self, Date):
        _translate = QtCore.QCoreApplication.translate
        Date.setWindowTitle(_translate("Date", "Dialog"))
        self.date_label.setText(_translate("Date", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">View or edit saved enquiries by date</span></p></body></html>"))
        self.view_bydate.setText(_translate("Date", "View Entries by Date"))
        self.edit_bydate.setText(_translate("Date", "Edit Entries by Date"))
        self.name_label.setText(_translate("Date", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">View or edit saved enquiries by name Of the person</span></p></body></html>"))
        self.query_name.setText(_translate("Date", "Name"))
        self.view_byname.setText(_translate("Date", "View Entries by Name"))
        self.edit_byname.setText(_translate("Date", "Edit Entries by Name"))
        self.View_All_Button.setText(_translate("Date", "View All Entries"))
        self.Close_Button.setText(_translate("Date", "Close"))
