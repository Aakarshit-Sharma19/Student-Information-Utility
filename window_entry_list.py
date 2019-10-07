from datetime import date
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout, QDialog
import data_mgmt as mg
import sys


class Button(QPushButton):
    def __init__(self,  obj, widgetobj):
        self.obj = obj
        self.name = self.obj.getName()
        super().__init__(self.name)
        self.widgetobj = widgetobj
        self.index = self.obj.getIndex()
    def click(self):
        self.widgetobj.finalEntry = self.obj
        self.widgetobj.close()


class Ui_Window(QDialog):
    def __init__(self, self_entry_data):
        super().__init__()
        self.finalEntry = mg.entry_data()
        self.index = -1 
        self.title = "Select from One of the Entries"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        formLayout = QFormLayout()
        groupBox = QGroupBox("Select the entry")
        self.entry_data = self_entry_data
        self.labelList = []
        self.comboList = []
        for i in range(len(self.entry_data)):
            self.labelList.append(QLabel(str(i+1)))
            self.comboList.append(Button(self.entry_data[i],self))
            self.comboList[i].clicked.connect(self.comboList[i].click)
            formLayout.addRow(self.labelList[i], self.comboList[i])

        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)
    def run(self):
        self.exec_()
        
    def getData(self):
        return self.finalEntry


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui_Window(50)
    sys.exit(app.exec_())

# To get the resolution of the available screen where app is the instance of the QApplication
# screen = app.primaryScreen()
# rect = screen.availableGeometry()
# print('Available: %d x %d' % (rect.width(), rect.height()))
