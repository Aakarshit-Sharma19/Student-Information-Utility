# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(392, 157)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.entry = QtWidgets.QPushButton(self.centralwidget)
        self.entry.setObjectName("entry")
        self.gridLayout.addWidget(self.entry, 2, 0, 1, 1)
        self.View_Edit = QtWidgets.QPushButton(self.centralwidget)
        self.View_Edit.setObjectName("View_Edit")
        self.gridLayout.addWidget(self.View_Edit, 2, 1, 1, 1)
        self.export_excel = QtWidgets.QPushButton(self.centralwidget)
        self.export_excel.setObjectName("export_excel")
        self.gridLayout.addWidget(self.export_excel, 3, 0, 1, 1)
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setObjectName("close")
        self.gridLayout.addWidget(self.close, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Student Information Utility"))
        self.label_2.setText(_translate("MainWindow", "Do you want to do a new entry or follow up to existing entry?"))
        self.entry.setText(_translate("MainWindow", "New Entry"))
        self.View_Edit.setText(_translate("MainWindow", "View or Edit an Existing Entry"))
        self.export_excel.setText(_translate("MainWindow", "Export To Excel"))
        self.close.setText(_translate("MainWindow", "Close"))
