import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QFileDialog
from PyQt5 import QtCore
import PyQt5.QtGui
import window_main as mainw
import window_entry as entw
import window_date_name as datew
import window_edit_selection as editw
import window_view_selection as vieww
import window_entry_list as listw
import data_mgmt as mg
import xlsxwriter



class select_date_name_ui:
    def __init__(self, view_ui_param, edit_ui_param):
        self.view_ui = view_ui_param
        self.edit_ui = edit_ui_param

        self.datenameui = QDialog()
        self.ui = datew.Ui_Date()
        self.ui.setupUi(self.datenameui)
        self.datenameui.setWindowTitle(
            "Search Existing Entries by Name or Date")

        self.EntryName = ''

        self.ui.edit_bydate.clicked.connect(self.EditByDate)
        self.ui.edit_byname.clicked.connect(self.EditByName)

        self.ui.view_bydate.clicked.connect(self.ViewByDate)
        self.ui.view_byname.clicked.connect(self.ViewByName)

        self.ui.View_All_Button.clicked.connect(self.ViewAll)
        self.ui.Close_Button.clicked.connect(self.datenameui.close)

    def run(self):
        self.datenameui.exec_()

    def create_entry_list(self, self_entry_data):
        self.entry_list_ui = listw.Ui_Window(self_entry_data)

    def EditByDate(self):
        self.data = mg.get_data_by_datename(
            self.ui.query_date.date().toPyDate())
        self.EditList()

    def EditByName(self):
        self.data = mg.get_data_by_name(self.ui.query_name.text())
        self.EditList()

    def ViewByDate(self):
        self.data = mg.get_data_by_datename(
            self.ui.query_date.date().toPyDate())
        self.ViewList()

    def ViewByName(self):
        self.data = mg.get_data_by_name(self.ui.query_name.text())
        self.ViewList()

    def ViewAll(self):
        self.data = mg.get_all()
        self.ViewList()

    def EditList(self):
        if self.data != []:
            print(self.data)
            self.create_entry_list(self.data)
            self.entry_list_ui.run()
            self.Entry = self.entry_list_ui.getData()
            if self.Entry.getIndex()!=0:
                self.edit_ui.setData(self.Entry)
                self.Edit()

    def Edit(self):
        self.edit_ui.run()

    def ViewList(self):
        if self.data != []:
            print(self.data)
            self.create_entry_list(self.data)
            self.entry_list_ui.run()
            self.Entry = self.entry_list_ui.getData()
            if self.Entry.getIndex()!=0:
                self.View()

    def View(self):
        self.ui.retranslateUi(self.datenameui)
        self.view_ui.setData(self.Entry)
        self.view_ui.run()

class edit_selection_ui:
    def __init__(self):
        self.editui = QDialog()
        self.editui.setWindowTitle("Edit the existing Entry")
        self.ui = editw.Ui_Dialog()
        self.ui.setupUi(self.editui)

        self.ui.delete_entry.clicked.connect(self.delete)
        self.ui.save_entry.clicked.connect(self.confirm_entry)
        self.ui.cancel.clicked.connect(self.editui.close)

        self.create_mbox()


    def mbox_text(self, string="The Edited Entry Has Been Updated"):
        self.mbox.setText(string)

    def create_mbox(self):
        self.mbox = QMessageBox()
        self.mbox_text()
        self.mbox.setDetailedText("Press 'ok' or 'cancel' to continue")
        self.mbox.setStandardButtons(QMessageBox.Ok)


    def setData(self, info):
        self.info = info
        self.index = info.getIndex()
        print(self.index)
        self.ui.StuName.setText(self.info.name)
        self.ui.StuAddress.setText(self.info.address)
        self.ui.StuPhone.setText(self.info.Phone_Number)
        self.ui.Stu_Interest.setText(self.info.Area_of_Interest)
        self.ui.StuDate.setDate(self.info.Date_Of_Enquiry)
        self.ui.Remarks.setPlainText(self.info.Remarks)

    def run(self):
        self.editui.exec_()

    def confirm_entry(self):
        self.update()
        self.editui.close()

    def delete(self):
        self.mbox_text("The following Entry has been Deleted")
        mg.delete(self.info.getIndex())
        self.confirm_dialog()
        self.mbox_text()
        self.editui.close()
    def update(self):

        self.info = mg.entry_data()
        self.info.name = self.ui.StuName.text()
        self.info.address = self.ui.StuAddress.text()
        self.info.Phone_Number = self.ui.StuPhone.text()
        self.info.Area_of_Interest = self.ui.Stu_Interest.text()
        self.info.Date_Of_Enquiry = self.ui.StuDate.date(
        ).toPyDate()  # .currentDate().toPyDate()
        self.info.Remarks = self.ui.Remarks.toPlainText()
        self.info.setIndex(self.index)

        mg.details(self.info)
        mg.update_data(self.info, self.info.getIndex())
        # print(self.ui.Stu_date.date().currentDate().toString())
        self.confirm_dialog()

    def confirm_dialog(self):
        self.mbox.exec_()

class view_selection_ui():
    def __init__(self,):
        self.viewui = QDialog()
        self.ui = vieww.Ui_Dialog()
        self.ui.setupUi(self.viewui)
        self.ui.OK_Button.clicked.connect(self.viewui.close)

    def setData(self, Entry):
        print('Index', Entry.getIndex())
        self.ui.StuName.setText(Entry.name)
        self.ui.StuAddress.setText(Entry.address)
        self.ui.Interest.setText(Entry.Area_of_Interest)
        self.ui.StuPhone.setText(Entry.Phone_Number)
        self.ui.StuDate.setText(Entry.Date_Of_Enquiry.strftime('%d/%m/%y'))
        self.ui.Remarks.setPlainText(Entry.Remarks)

    def run(self):
        print('Viewed', self.ui.StuName.text())
        self.viewui.exec_()



class entry_ui():
    def __init__(self):
        self.entryui = QDialog()
        self.ui = entw.Ui_Dialog()
        self.ui.setupUi(self.entryui)
        self.ui.Save_New_Button.clicked.connect(self.new_entry)
        self.ui.Save_Exit_Button.clicked.connect(self.confirm_entry)
        self.ui.Cancel_Button.clicked.connect(self.entryui.close)

        self.ui.Save_Status.setText(f"Today's Date: {self.ui.StuDate.date().currentDate().toString()}")
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
        info.Date_Of_Enquiry = self.ui.StuDate.date(
        ).toPyDate()  # .currentDate().toPyDate()
        info.Remarks = self.ui.Remarks.toPlainText()

        mg.details(info)
        mg.push_data(info)
        self.save_dialog()

    def new_entry(self):
        self.store_entry_db()
        print("Last Entry Saved")
        self.ui.retranslateUi(self.entryui)
        self.ui.StuDate.setDate(self.ui.StuDate.date().currentDate())

    def save_dialog(self):

        self.save_mbox.exec_()



class export_excel:
    def __init__(self, file):
        # create workboot / file data.xlsx
        if file != None:
            print('File Created',file)
            self.wb = xlsxwriter.Workbook(file)
            self.sheet = self.wb.add_worksheet('Sheet 1')
        self.row = 1
        self.column = 0
    def export(self, entry_data):
        print('Export Started')
        self.entry_data = entry_data
        print('\n\n\n\n',self.sheet,'\n\n\n')
        self.writeFirstRow()
        for x in entry_data:
            self.writeRow(x,self.row)
            self.row+=1
        self.wb.close()
    def writeFirstRow(self):
        self.sheet.write_string(0,self.column,'ID')
        self.sheet.write_string(0,self.column+1,'Date')
        self.sheet.write_string(0,self.column+2,'Name')
        self.sheet.write_string(0,self.column+3,'Address')
        self.sheet.write_string(0,self.column+4,'Phone')
        self.sheet.write_string(0,self.column+5,'Interests')
        self.sheet.write_string(0,self.column+6,'Remarks')
    def writeRow(self, entry, row):
        self.sheet.write(row,self.column,entry.index)
        self.sheet.write(row,self.column+1,entry.Date_Of_Enquiry.strftime('%d/%m/%y'))
        self.sheet.write(row,self.column+2,entry.name)
        self.sheet.write(row,self.column+3,entry.address)
        self.sheet.write(row,self.column+4,entry.Phone_Number)
        self.sheet.write(row,self.column+5,entry.Area_of_Interest)
        self.sheet.write(row,self.column+6,entry.Remarks)



class main_ui:
    def __init__(self, ent_ui_param, edit_ui_param,  date_ui_param, ):  # (view_ui_param)
        self.main_wind = QMainWindow()
        self.ui = mainw.Ui_MainWindow()
        self.ui.setupUi(self.main_wind)
        self.main_wind.showNormal()
        self.main_wind.setWindowTitle(
            "Student Information Utility - Created By Aakarshit Sharma")
        self.main_wind.setWindowIcon(PyQt5.QtGui.QIcon('student.png'))

        self.ent_ui = ent_ui_param

        self.edit_ui = edit_ui_param

        self.date_ui = date_ui_param

        self.run()

    def export(self):

        file = self.saveFileDialog()
        if file!=None:
            self.export_excel = export_excel(file)
            self.export_excel.export(mg.get_all())

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(
            self.main_wind, "QFileDialog.getSaveFileName()", "", "Excel Files (*.xlsx)", options=options)
        if fileName != '':
            return (fileName+'.xlsx')
        else:
            return None

    def run(self):
        self.ui.entry.clicked.connect(self.ent_ui.run)
        self.ui.close.clicked.connect(sys.exit)
        self.ui.View_Edit.clicked.connect(self.date_ui.run)
        self.ui.export_excel.clicked.connect(self.export)



if __name__ == '__main__':

    app = QApplication(sys.argv)

    ent_ui = entry_ui()
    edit_ui = edit_selection_ui()
    view_ui = view_selection_ui()
    date_ui = select_date_name_ui(view_ui, edit_ui)
    main_ui = main_ui(ent_ui, edit_ui, date_ui)  # view_ui
    sys.exit(app.exec_())
