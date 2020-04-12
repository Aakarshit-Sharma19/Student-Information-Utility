#!/usr/bin/python3
import sys
import PyQt5.QtGui
import xlsxwriter
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QFileDialog, QLabel, QGridLayout, \
    QPushButton

import data_mgmt as mg
import window_date_name as datew
import window_edit_selection as editw
import window_entry_list as listw
import window_main as mainw
import window_new_entry as entw
import window_view_selection as vieww


class ErrorDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.MessageLabel = QLabel()
        self.MessageLabel.setMinimumHeight(200)
        self.button = QPushButton()
        self.button.setMinimumHeight(50)
        self.button.setText('Ok')
        self.button.clicked.connect(self.close)
        self.grid = QGridLayout(self)
        self.grid.addWidget(self.MessageLabel)
        self.grid.addWidget(self.button)

    def show_message(self, message):
        self.MessageLabel.setText(message)
        self.exec_()


class SelectByDateNameUi(QDialog):
    def __init__(self, view_ui_param, edit_ui_param):
        super().__init__()
        self.view_ui = view_ui_param
        self.edit_ui = edit_ui_param

        self.ui = datew.Ui_Date()
        self.ui.setupUi(self)
        self.setWindowTitle(
            "Search Existing Entries by Name or Date")

        self.EntryName = ''

        self.ui.edit_bydate.clicked.connect(self.edit_by_date)
        self.ui.edit_byname.clicked.connect(self.edit_by_name)

        self.ui.view_bydate.clicked.connect(self.view_by_date)
        self.ui.view_byname.clicked.connect(self.view_by_name)

        self.ui.View_All_Button.clicked.connect(self.view_all)
        self.ui.Close_Button.clicked.connect(self.close)

        self.error_dialog = ErrorDialog()

    def run(self):
        self.exec_()

    def create_entry_list(self, self_entry_data):
        self.entry_list_ui = listw.UiWindow(self_entry_data)

    def edit_by_date(self):
        self.data = mg.get_data_by_datename(
            self.ui.query_date.date().toPyDate())
        self.edit_list()

    def edit_by_name(self):
        self.data = mg.get_data_by_name(self.ui.query_name.text())
        self.edit_list()

    def view_by_date(self):
        self.data = mg.get_data_by_datename(
            self.ui.query_date.date().toPyDate())
        self.view_list()

    def view_by_name(self):
        self.data = mg.get_data_by_name(self.ui.query_name.text())
        self.view_list()

    def view_all(self):
        self.data = mg.get_all()
        self.view_list()

    def edit_list(self):
        if self.data != []:
            print(self.data)
            self.create_entry_list(self.data)
            self.entry_list_ui.run()
            self.Entry = self.entry_list_ui.getData()
            if self.Entry.getIndex() != 0:
                self.edit_ui.set_data(self.Entry)
                self.edit_ui.run()
        else:
            self.error_dialog.show_message('Could not Find Any Entries. Please search with different parametrs')

    def view_list(self):
        if self.data != []:
            print(self.data)
            self.create_entry_list(self.data)
            self.entry_list_ui.run()
            self.Entry = self.entry_list_ui.getData()
            if self.Entry.getIndex() != 0:
                self.view()
                if self.view_ui.edit_bool:
                    self.edit_ui.set_data(self.Entry)
                    self.edit_ui.run()
        else:
            self.error_dialog.show_message('Could not Find Any Entries. Please search with different parametrs')

    def view(self):
        self.ui.retranslateUi(self)
        self.view_ui.set_data(self.Entry)
        self.view_ui.run()


class EditSelectionUi(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit the existing Entry")
        self.ui = editw.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.Delete_Button.clicked.connect(self.delete)
        self.ui.Save_Exit_Button.clicked.connect(self.confirm_entry)
        self.ui.Cancel_Button.clicked.connect(self.close)

        self.confirm_mbox = QMessageBox()
        self.confirm_mbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.confirm_mbox.setDefaultButton(QMessageBox.No)

    def set_data(self, info):
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
        self.exec_()

    def confirm_entry(self):
        self.confirm_mbox.setText("Do you want to confirm the changes made to the entry?")
        if self.confirm_mbox.exec_() == QMessageBox.Yes:
            self.update()
            self.close()

    def delete(self):
        self.confirm_mbox.setText("Do you want to delete this entry ")
        if self.confirm_mbox.exec_() == QMessageBox.Yes:
            mg.delete(self.info.getIndex())
            self.close()

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


class ViewSelectionUi(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = vieww.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.OK_Button.clicked.connect(self.close)
        self.edit_bool = False
        self.ui.Edit_Button.clicked.connect(self.edit_bool_true)

    def edit_bool_true(self):
        self.edit_bool = True
        self.close()

    def set_data(self, Entry):
        print('Index', Entry.getIndex())
        self.ui.StuName.setText(Entry.name)
        self.ui.StuAddress.setText(Entry.address)
        self.ui.Interest.setText(Entry.Area_of_Interest)
        self.ui.StuPhone.setText(Entry.Phone_Number)
        self.ui.StuDate.setText(Entry.Date_Of_Enquiry.strftime('%d/%m/%y'))
        self.ui.Remarks.setPlainText(Entry.Remarks)

    def run(self):
        print('Viewed Student:', self.ui.StuName.text())
        self.exec_()


class EntryUi(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = entw.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.Save_New_Button.clicked.connect(self.new_entry)
        self.ui.Save_Exit_Button.clicked.connect(self.confirm_entry)
        self.ui.Cancel_Button.clicked.connect(self.close)

        self.ui.Save_Status.setText("Today's Date: {}".format(self.ui.StuDate.date().currentDate().toString()))
        self.ui.StuDate.setDate(self.ui.StuDate.date().currentDate())

        self.save_mbox = QMessageBox()
        self.save_mbox.setText("The Entry Has Been Saved")
        self.save_mbox.setDetailedText("Press 'ok' or 'cancel' to continue")
        self.save_mbox.setStandardButtons(QMessageBox.Ok)

    def run(self):
        self.ui.retranslateUi(self)
        self.showMaximized()

    def confirm_entry(self):
        self.store_entry_db()
        self.close()

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
        self.ui.retranslateUi(self)
        self.ui.StuDate.setDate(self.ui.StuDate.date().currentDate())

    def save_dialog(self):
        self.save_mbox.exec_()


class ExportExcel:
    def __init__(self, file):
        # create workboot / file data.xlsx
        if file != None:
            print('File Created', file)
            self.wb = xlsxwriter.Workbook(file)
            self.sheet = self.wb.add_worksheet('Sheet 1')
        self.row = 1
        self.column = 0

    def export(self, entry_data):
        print('Export Started')
        self.entry_data = entry_data
        print('\n\n\n\n', self.sheet, '\n\n\n')
        self.write_first_row()
        for x in entry_data:
            self.write_row(x, self.row)
            self.row += 1
        self.wb.close()

    def write_first_row(self):
        self.sheet.write_string(0, self.column, 'ID')
        self.sheet.write_string(0, self.column + 1, 'Date')
        self.sheet.write_string(0, self.column + 2, 'Name')
        self.sheet.write_string(0, self.column + 3, 'Address')
        self.sheet.write_string(0, self.column + 4, 'Phone')
        self.sheet.write_string(0, self.column + 5, 'Interests')
        self.sheet.write_string(0, self.column + 6, 'Remarks')

    def write_row(self, entry, row):
        self.sheet.write(row, self.column, entry.index)
        self.sheet.write(row, self.column + 1, entry.Date_Of_Enquiry.strftime('%d/%m/%y'))
        self.sheet.write(row, self.column + 2, entry.name)
        self.sheet.write(row, self.column + 3, entry.address)
        self.sheet.write(row, self.column + 4, entry.Phone_Number)
        self.sheet.write(row, self.column + 5, entry.Area_of_Interest)
        self.sheet.write(row, self.column + 6, entry.Remarks)


class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = mainw.Ui_MainWindow()
        self.ui.setupUi(self)
        self.showNormal()
        self.setWindowTitle(
            "Student Information Utility - Created By Aakarshit Sharma")
        self.setWindowIcon(PyQt5.QtGui.QIcon('student.png'))
        self.run()

    def export(self):

        file = self.save_file_dialog()
        if file != None:
            self.export_excel = ExportExcel(file)
            self.export_excel.export(mg.get_all())

    def save_file_dialog(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(
            self, "QFileDialog.getSaveFileName()", "", "Excel Files (*.xlsx)", options=options)
        if fileName != '':
            return fileName  # + '.xlsx'
        else:
            return None

    def run(self):
        self.ui.entry.clicked.connect(ent_ui.run)
        self.ui.close.clicked.connect(sys.exit)
        self.ui.View_Edit.clicked.connect(date_ui.run)
        self.ui.export_excel.clicked.connect(self.export)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ent_ui = EntryUi()
    edit_ui = EditSelectionUi()
    view_ui = ViewSelectionUi()
    date_ui = SelectByDateNameUi(view_ui, edit_ui)
    main_ui = MainUi()
    sys.exit(app.exec_())
