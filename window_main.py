# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(836, 425)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 4)
        self.entry = QtWidgets.QPushButton(self.centralwidget)
        self.entry.setMinimumSize(QtCore.QSize(200, 50))
        self.entry.setObjectName("entry")
        self.gridLayout_2.addWidget(self.entry, 1, 0, 1, 1)
        self.View_Edit = QtWidgets.QPushButton(self.centralwidget)
        self.View_Edit.setMinimumSize(QtCore.QSize(200, 50))
        self.View_Edit.setObjectName("View_Edit")
        self.gridLayout_2.addWidget(self.View_Edit, 1, 1, 1, 1)
        self.export_excel = QtWidgets.QPushButton(self.centralwidget)
        self.export_excel.setMinimumSize(QtCore.QSize(200, 50))
        self.export_excel.setObjectName("export_excel")
        self.gridLayout_2.addWidget(self.export_excel, 1, 2, 1, 1)
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setMinimumSize(QtCore.QSize(200, 50))
        self.close.setObjectName("close")
        self.gridLayout_2.addWidget(self.close, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Student Information Utility</span></p><p align=\"center\"><br/>Welcome to the Enquiry Utility.</p><p align=\"center\">You can create a new entry, view or edit the existing entries and also export them as excel files.</p><p align=\"center\"><br/></p></body></html>"))
        self.entry.setText(_translate("MainWindow", "New Entry"))
        self.View_Edit.setText(_translate(
            "MainWindow", "View or Edit existing entries"))
        self.export_excel.setText(_translate("MainWindow", "Export To Excel"))
        self.close.setText(_translate("MainWindow", "Close"))
