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
        MainWindow.resize(460, 176)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 171, 20))
        self.label.setObjectName("label")
        self.entry = QtWidgets.QPushButton(self.centralwidget)
        self.entry.setGeometry(QtCore.QRect(20, 80, 190, 24))
        self.entry.setObjectName("entry")
        self.View_Edit = QtWidgets.QPushButton(self.centralwidget)
        self.View_Edit.setGeometry(QtCore.QRect(250, 80, 190, 24))
        self.View_Edit.setObjectName("View_Edit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 381, 18))
        self.label_2.setObjectName("label_2")
        self.export_excel = QtWidgets.QPushButton(self.centralwidget)
        self.export_excel.setGeometry(QtCore.QRect(20, 120, 190, 24))
        self.export_excel.setObjectName("export_excel")
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setGeometry(QtCore.QRect(250, 120, 190, 24))
        self.close.setObjectName("close")
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
        self.entry.setText(_translate("MainWindow", "New Entry"))
        self.View_Edit.setText(_translate("MainWindow", "View or Edit an Existing Entry"))
        self.label_2.setText(_translate("MainWindow", "Do you want to do a new entry or follow up to existing entry?"))
        self.export_excel.setText(_translate("MainWindow", "Export To Excel"))
        self.close.setText(_translate("MainWindow", "close"))
