# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(763, 438)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_StuName = QtWidgets.QLabel(Dialog)
        self.label_StuName.setMinimumSize(QtCore.QSize(0, 50))
        self.label_StuName.setObjectName("label_StuName")
        self.gridLayout.addWidget(self.label_StuName, 0, 0, 1, 1)
        self.StuName = QtWidgets.QLabel(Dialog)
        self.StuName.setMinimumSize(QtCore.QSize(600, 50))
        self.StuName.setObjectName("StuName")
        self.gridLayout.addWidget(self.StuName, 0, 1, 1, 2)
        self.label_StuAddress = QtWidgets.QLabel(Dialog)
        self.label_StuAddress.setMinimumSize(QtCore.QSize(0, 50))
        self.label_StuAddress.setObjectName("label_StuAddress")
        self.gridLayout.addWidget(self.label_StuAddress, 1, 0, 1, 1)
        self.StuAddress = QtWidgets.QLabel(Dialog)
        self.StuAddress.setMinimumSize(QtCore.QSize(600, 50))
        self.StuAddress.setText("")
        self.StuAddress.setObjectName("StuAddress")
        self.gridLayout.addWidget(self.StuAddress, 1, 1, 1, 2)
        self.label_Interest = QtWidgets.QLabel(Dialog)
        self.label_Interest.setMinimumSize(QtCore.QSize(0, 50))
        self.label_Interest.setObjectName("label_Interest")
        self.gridLayout.addWidget(self.label_Interest, 2, 0, 1, 1)
        self.Interest = QtWidgets.QLabel(Dialog)
        self.Interest.setMinimumSize(QtCore.QSize(600, 50))
        self.Interest.setText("")
        self.Interest.setObjectName("Interest")
        self.gridLayout.addWidget(self.Interest, 2, 1, 1, 2)
        self.label_StuPhone = QtWidgets.QLabel(Dialog)
        self.label_StuPhone.setMinimumSize(QtCore.QSize(0, 50))
        self.label_StuPhone.setObjectName("label_StuPhone")
        self.gridLayout.addWidget(self.label_StuPhone, 3, 0, 1, 1)
        self.StuPhone = QtWidgets.QLabel(Dialog)
        self.StuPhone.setMinimumSize(QtCore.QSize(600, 50))
        self.StuPhone.setText("")
        self.StuPhone.setObjectName("StuPhone")
        self.gridLayout.addWidget(self.StuPhone, 3, 1, 1, 2)
        self.label_StuDate = QtWidgets.QLabel(Dialog)
        self.label_StuDate.setMinimumSize(QtCore.QSize(0, 50))
        self.label_StuDate.setObjectName("label_StuDate")
        self.gridLayout.addWidget(self.label_StuDate, 4, 0, 1, 1)
        self.StuDate = QtWidgets.QLabel(Dialog)
        self.StuDate.setMinimumSize(QtCore.QSize(600, 50))
        self.StuDate.setText("")
        self.StuDate.setObjectName("StuDate")
        self.gridLayout.addWidget(self.StuDate, 4, 1, 1, 2)
        self.label_Remarks = QtWidgets.QLabel(Dialog)
        self.label_Remarks.setObjectName("label_Remarks")
        self.gridLayout.addWidget(self.label_Remarks, 5, 0, 1, 1)
        self.Edit_Button = QtWidgets.QPushButton(Dialog)
        self.Edit_Button.setMinimumSize(QtCore.QSize(200, 50))
        self.Edit_Button.setObjectName("Edit_Button")
        self.gridLayout.addWidget(self.Edit_Button, 6, 1, 1, 1)
        self.OK_Button = QtWidgets.QPushButton(Dialog)
        self.OK_Button.setMinimumSize(QtCore.QSize(200, 50))
        self.OK_Button.setObjectName("OK_Button")
        self.gridLayout.addWidget(self.OK_Button, 6, 2, 1, 1)
        self.Remarks = QtWidgets.QTextBrowser(Dialog)
        self.Remarks.setMinimumSize(QtCore.QSize(600, 0))
        self.Remarks.setObjectName("Remarks")
        self.gridLayout.addWidget(self.Remarks, 5, 1, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New Entry"))
        self.label_StuName.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Name:</span></p></body></html>"))
        self.StuName.setText(_translate("Dialog", "\'"))
        self.label_StuAddress.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Address:</span></p></body></html>"))
        self.label_Interest.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Area of Interest</span></p></body></html>"))
        self.label_StuPhone.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Phone Number</span></p></body></html>"))
        self.label_StuDate.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Date</span></p></body></html>"))
        self.label_Remarks.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Remarks</span></p></body></html>"))
        self.Edit_Button.setText(_translate("Dialog", "Edit This Entry"))
        self.OK_Button.setText(_translate("Dialog", "OK"))
        self.Remarks.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Remarks or extra information pertaining to the student.</p></body></html>"))
