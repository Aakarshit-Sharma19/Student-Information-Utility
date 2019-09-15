import sys, time 
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
import window_main as mainw
import window_entry as entw
import window_edit_selection as editw
import window_view_selection as vieww
import data_mgmt as mg


class edit_selection_ui:
    def __init__(self):
        self.editui = QDialog()
        self.ui = editw.Ui_Dialog()
        self.ui.setupUi(self.editui)

    def run(self):
        self.editui.showNormal()


class view_selection_ui():
    def __init__(self):
        self.viewui = QDialog()
        self.ui = vieww.Ui_Dialog()
        self.ui.setupUi(self.viewui)
    def run(self):
        self.viewui.showNormal()


class entry_ui():
    def __init__(self):
        self.entryui = QDialog()
        self.ui = entw.Ui_Dialog()
        self.ui.setupUi(self.entryui)
        self.repeat = 0
        self.ui.pushButton.clicked.connect(self.new_entry)
        self.ui.pushButton_2.clicked.connect(self.confirm_entry)
        self.ui.pushButton_3.clicked.connect(self.entryui.close)

        self.ui.Save_Status.setText(
            f"Today's Date: {self.ui.Stu_date.date().currentDate().toString()}")
        self.ui.Stu_date.setDate(self.ui.Stu_date.date().currentDate())

        self.save_mbox = QMessageBox()
        self.save_mbox.setText("The Entry Has Been Saved")
        self.save_mbox.setDetailedText("Press 'ok' or 'cancel' to continue")
        self.save_mbox.setStandardButtons(QMessageBox.Ok)

    def run(self):
        self.entryui.showNormal()

    def confirm_entry(self):
        self.store_entry_db()
        self.entryui.close()

    def store_entry_db(self):

        info = mg.entry_data()
        info.name = self.ui.StuName.text()
        info.address = self.ui.StuAddress.text()
        info.Phone_Number = self.ui.Stu_Phone.text()
        info.Area_of_Interest = self.ui.Interest.text()
        info.Date_Of_Enquiry = self.ui.Stu_date.date().toPyDate()  # .currentDate().toPyDate()
        info.Remarks = self.ui.Remarks.toPlainText()

        mg.details(info)
        mg.push_data(info)
        # print(self.ui.Stu_date.date().currentDate().toString())
        self.save_dialog()

    def new_entry(self):
        self.store_entry_db()
        print("Last Entry Saved")
        self.ui.retranslateUi(self.entryui)
        self.ui.Stu_date.setDate(self.ui.Stu_date.date().currentDate())

   
    # def update_savestatus(self):
    #     self.ui.Save_Status.setText('  ')
    #     print('done')

    def save_dialog(self):

        self.save_mbox.exec_()


class main_ui:
    def __init__(self, ent_ui_param, edit_ui_param, view_ui_param):
        self.main_wind = QMainWindow()
        self.ui = mainw.Ui_MainWindow()
        self.ui.setupUi(self.main_wind)
        self.main_wind.showNormal()

        self.ent_ui = ent_ui_param

        self.edit_ui = edit_ui_param

        self.view_ui = view_ui_param

        self.run()

    def run(self):
        self.ui.entry.clicked.connect(self.ent_ui.run)
        self.ui.close.clicked.connect(sys.exit)
        self.ui.View_Edit.clicked.connect(self.view_ui.run)
        self.ui.export_excel.clicked.connect(mg.show_all)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    ent_ui = entry_ui()
    edit_ui = edit_selection_ui()
    view_ui = view_selection_ui()
    main_ui = main_ui(ent_ui, edit_ui, view_ui)
    sys.exit(app.exec_())
