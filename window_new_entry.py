# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/aakarshit/Desktop/Student-Information-Utility/UI Files/entry.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(886, 438)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_StuName = QtWidgets.QLabel(Dialog)
        self.label_StuName.setMinimumSize(QtCore.QSize(0, 50))
        self.label_StuName.setObjectName("label_StuName")
        self.gridLayout.addWidget(self.label_StuName, 0, 0, 1, 1)
        self.StuName = QtWidgets.QLineEdit(Dialog)
        self.StuName.setMinimumSize(QtCore.QSize(600, 50))
        self.StuName.setObjectName("StuName")
        self.gridLayout.addWidget(self.StuName, 0, 1, 1, 3)
        self.label_StuAddress = QtWidgets.QLabel(Dialog)
        self.label_StuAddress.setMinimumSize(QtCore.QSize(0, 50))
        self.label_StuAddress.setObjectName("label_StuAddress")
        self.gridLayout.addWidget(self.label_StuAddress, 1, 0, 1, 1)
        self.StuAddress = QtWidgets.QLineEdit(Dialog)
        self.StuAddress.setMinimumSize(QtCore.QSize(600, 50))
        self.StuAddress.setObjectName("StuAddress")
        self.gridLayout.addWidget(self.StuAddress, 1, 1, 1, 3)
        self.label_Interest = QtWidgets.QLabel(Dialog)
        self.label_Interest.setMinimumSize(QtCore.QSize(0, 50))
        self.label_Interest.setObjectName("label_Interest")
        self.gridLayout.addWidget(self.label_Interest, 2, 0, 1, 1)
        self.Interest = QtWidgets.QLineEdit(Dialog)
        self.Interest.setMinimumSize(QtCore.QSize(600, 50))
        self.Interest.setObjectName("Interest")
        self.gridLayout.addWidget(self.Interest, 2, 1, 1, 3)
        self.label_StuPhone = QtWidgets.QLabel(Dialog)
        self.label_StuPhone.setMinimumSize(QtCore.QSize(0, 50))
        self.label_StuPhone.setObjectName("label_StuPhone")
        self.gridLayout.addWidget(self.label_StuPhone, 3, 0, 1, 1)
        self.StuPhone = QtWidgets.QLineEdit(Dialog)
        self.StuPhone.setMinimumSize(QtCore.QSize(600, 50))
        self.StuPhone.setObjectName("StuPhone")
        self.gridLayout.addWidget(self.StuPhone, 3, 1, 1, 3)
        self.label_StuDate = QtWidgets.QLabel(Dialog)
        self.label_StuDate.setMinimumSize(QtCore.QSize(0, 50))
        self.label_StuDate.setObjectName("label_StuDate")
        self.gridLayout.addWidget(self.label_StuDate, 4, 0, 1, 1)
        self.StuDate = QtWidgets.QDateEdit(Dialog)
        self.StuDate.setMinimumSize(QtCore.QSize(600, 50))
        self.StuDate.setObjectName("StuDate")
        self.gridLayout.addWidget(self.StuDate, 4, 1, 1, 3)
        self.label_Remarks = QtWidgets.QLabel(Dialog)
        self.label_Remarks.setObjectName("label_Remarks")
        self.gridLayout.addWidget(self.label_Remarks, 5, 0, 1, 1)
        self.Remarks = QtWidgets.QTextEdit(Dialog)
        self.Remarks.setMinimumSize(QtCore.QSize(600, 0))
        self.Remarks.setObjectName("Remarks")
        self.gridLayout.addWidget(self.Remarks, 5, 1, 1, 3)
        self.Save_Status = QtWidgets.QLabel(Dialog)
        self.Save_Status.setMinimumSize(QtCore.QSize(250, 50))
        self.Save_Status.setText("")
        self.Save_Status.setObjectName("Save_Status")
        self.gridLayout.addWidget(self.Save_Status, 6, 0, 1, 1)
        self.Save_New_Button = QtWidgets.QPushButton(Dialog)
        self.Save_New_Button.setMinimumSize(QtCore.QSize(200, 50))
        self.Save_New_Button.setObjectName("Save_New_Button")
        self.gridLayout.addWidget(self.Save_New_Button, 6, 1, 1, 1)
        self.Save_Exit_Button = QtWidgets.QPushButton(Dialog)
        self.Save_Exit_Button.setMinimumSize(QtCore.QSize(200, 50))
        self.Save_Exit_Button.setObjectName("Save_Exit_Button")
        self.gridLayout.addWidget(self.Save_Exit_Button, 6, 2, 1, 1)
        self.Cancel_Button = QtWidgets.QPushButton(Dialog)
        self.Cancel_Button.setMinimumSize(QtCore.QSize(200, 50))
        self.Cancel_Button.setObjectName("Cancel_Button")
        self.gridLayout.addWidget(self.Cancel_Button, 6, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New Entry"))
        self.label_StuName.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Name:</span></p></body></html>"))
        self.StuName.setText(_translate("Dialog", "Type the student\'s name here"))
        self.label_StuAddress.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Address:</span></p></body></html>"))
        self.StuAddress.setText(_translate("Dialog", "Student\'s Address"))
        self.label_Interest.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Area of Interest</span></p></body></html>"))
        self.Interest.setText(_translate("Dialog", "In what field,  the student is interested? Eg.:- Hospitality,Hotel Management"))
        self.label_StuPhone.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Phone Number</span></p></body></html>"))
        self.StuPhone.setText(_translate("Dialog", "Enter Phone Number"))
        self.label_StuDate.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Date</span></p></body></html>"))
        self.label_Remarks.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Remarks</span></p></body></html>"))
        self.Remarks.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Remarks or extra information pertaining to the student.</p></body></html>"))
        self.Save_New_Button.setText(_translate("Dialog", "Save and Create new Entry"))
        self.Save_Exit_Button.setText(_translate("Dialog", "Save and Exit"))
        self.Cancel_Button.setText(_translate("Dialog", "Cancel"))
