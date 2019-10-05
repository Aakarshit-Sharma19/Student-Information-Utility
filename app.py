import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5 import QtCore
import PyQt5.QtGui
import window_main as mainw
import window_entry as entw
import window_date_name as datew
import window_edit_selection as editw
import window_view_selection as vieww
import window_entry_list as listw
import data_mgmt as mg





class edit_selection_ui:
    def __init__(self):
        self.editui = QDialog()
        self.editui.setWindowTitle("Edit the existing Entry")
        self.ui = editw.Ui_Dialog()
        self.ui.setupUi(self.editui)
        self.save_mbox = QMessageBox()
        self.save_mbox.setText("The Edited Entry Has Been Saved")
        self.save_mbox.setDetailedText("Press 'ok' or 'cancel' to continue")
        self.save_mbox.setStandardButtons(QMessageBox.Ok)

    def setData(self,info_obj):
        self.ui.StuName.setText(info_obj.name)
        self.ui.StuAddress.setText(info_obj.address)
        self.ui.Stu_Phone.setText(info_obj.Phone_Number)
        self.ui.Interest.setText(info_obj.Area_of_Interest)
        self.ui.Stu_date.setDate(info_obj.Stu_date)
        self.ui.Remarks.setText(info_obj.Remarks)


    def run(self):
        self.editui.showNormal()

    def confirm_entry(self):
        self.store_entry_db()
        self.editui.close()

    def store_entry_db(self):

        # info = mg.entry_data()
        # info.name = self.ui.StuName.text()
        # info.address = self.ui.StuAddress.text()
        # info.Phone_Number = self.ui.Stu_Phone.text()
        # info.Area_of_Interest = self.ui.Interest.text()
        # info.Date_Of_Enquiry = self.ui.Stu_date.date().toPyDate()  # .currentDate().toPyDate()
        # info.Remarks = self.ui.Remarks.toPlainText()

        # mg.details(info)
        # mg.push_data(info)
        # print(self.ui.Stu_date.date().currentDate().toString())
        self.save_dialog()
    
    def save_dialog(self):
        self.save_mbox.exec_()



class select_date_name_ui:
    def __init__(self, view_ui_param):
        self.view_ui = view_ui_param

        self.datenameui = QDialog()
        self.ui = datew.Ui_Date()
        self.ui.setupUi(self.datenameui)
        self.datenameui.setWindowTitle("Search Existing Entries by Name or Date")
        
        self.EntryName = ''

        self.ui.edit_bydate.clicked.connect(self.EditByDate)
        self.ui.edit_byname.clicked.connect(self.EditByName)
        
        self.ui.view_bydate.clicked.connect(self.ViewByDate)
        self.ui.view_byname.clicked.connect(self.ViewByName)
    
    def run(self):
        self.datenameui.exec_()
    def create_entry_list(self, self_entry_data):
            self.entry_list_ui = listw.Ui_Window(self_entry_data)
    def EditByDate(self):
        pass
    def EditByName(self):
        self.data =mg.get_data_by_name(self.ui.query_name.text())
        self.create_entry_list(self.data)
        self.entry_list_ui.run()
        self.EntryName = self.entry_list_ui.getName()
        print(self.EntryName)
    def ViewByDate(self):
        pass
    def ViewByName(self):
        self.data =mg.get_data_by_name(self.ui.query_name.text())
        self.create_entry_list(self.data)
        self.entry_list_ui.run()
        self.Entry = self.entry_list_ui.getData()
        print(self.Entry.getName())
        self.View()

    def View(self):
       
        self.view_ui.populate(self.Entry)
        self.view_ui.run()


class view_selection_ui():
    def __init__(self,):
        self.viewui = QDialog()
        self.ui = vieww.Ui_Dialog()
        self.ui.setupUi(self.viewui)
        self.ui.OK_Button.clicked.connect(self.viewui.close)
    def populate(self, Entry):
        self.ui.StuName.setText(Entry.name)
        self.ui.StuAddress.setText(Entry.address)
        self.ui.Interest.setText(Entry.Area_of_Interest)
        self.ui.StuPhone.setText(Entry.Phone_Number)
        self.ui.StuDate.setText(Entry.Date_Of_Enquiry.strftime('%d/%m/%y'))
        self.ui.Remarks.setPlainText(Entry.Remarks)
    def run(self):
        print('viewed')
        self.viewui.exec_()

class select_selection_ui():
    pass


class entry_ui():
    def __init__(self):
        self.entryui = QDialog()
        self.ui = entw.Ui_Dialog()
        self.ui.setupUi(self.entryui)
        self.ui.Save_New_Button.clicked.connect(self.new_entry)
        self.ui.Save_Exit_Button.clicked.connect(self.confirm_entry)
        self.ui.Cancel_Button.clicked.connect(self.entryui.close)

        self.ui.Save_Status.setText(
            f"Today's Date: {self.ui.StuDate.date().currentDate().toString()}")
        self.ui.StuDate.setDate(self.ui.StuDate.date().currentDate())

        self.save_mbox = QMessageBox()
        self.save_mbox.setText("The Entry Has Been Saved")
        self.save_mbox.setDetailedText("Press 'ok' or 'cancel' to continue")
        self.save_mbox.setStandardButtons(QMessageBox.Ok)

    def run(self):
        self.entryui.showMaximized()

    def confirm_entry(self):
        self.store_entry_db()
        self.entryui.close()

    def store_entry_db(self):

        info = mg.entry_data()
        info.name = self.ui.StuName.text()
        info.address = self.ui.StuAddress.text()
        info.Phone_Number = self.ui.StuPhone.text()
        info.Area_of_Interest = self.ui.Interest.text()
        info.Date_Of_Enquiry = self.ui.StuDate.date().toPyDate()  # .currentDate().toPyDate()
        info.Remarks = self.ui.Remarks.toPlainText()

        mg.details(info)
        mg.push_data(info)
        # print(self.ui.Stu_date.date().currentDate().toString())
        self.save_dialog()

    def new_entry(self):
        self.store_entry_db()
        print("Last Entry Saved")
        self.ui.retranslateUi(self.entryui)
        self.ui.StuDate.setDate(self.ui.StuDate.date().currentDate())
        

    def save_dialog(self):

        self.save_mbox.exec_()


class main_ui:
    def __init__(self, ent_ui_param, edit_ui_param,  date_ui_param, ):#(view_ui_param)
        self.main_wind = QMainWindow()
        self.ui = mainw.Ui_MainWindow()
        self.ui.setupUi(self.main_wind)
        self.main_wind.showNormal()
        self.main_wind.setWindowTitle("Student Information Utility")
        self.main_wind.setWindowIcon(PyQt5.QtGui.QIcon('student.png'))

        self.ent_ui = ent_ui_param

        self.edit_ui = edit_ui_param

        # self.view_ui = view_ui_param

        self.date_ui = date_ui_param
        
        self.run()

    def run(self):
        self.ui.entry.clicked.connect(self.ent_ui.run)
        self.ui.close.clicked.connect(sys.exit)
        self.ui.View_Edit.clicked.connect(self.date_ui.run)
        self.ui.export_excel.clicked.connect(mg.show_all)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    ent_ui = entry_ui()
    edit_ui = edit_selection_ui()
    view_ui = view_selection_ui()
    date_ui = select_date_name_ui(view_ui)
    main_ui = main_ui(ent_ui, edit_ui, date_ui)#view_ui
    sys.exit(app.exec_())
