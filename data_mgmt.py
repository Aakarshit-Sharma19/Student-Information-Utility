from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
from datetime import date, datetime
import sqlite3
import os
# To be Run everytime this module is used
file = '.entries.db'
file = os.path.expanduser('~/'+file)
conn = sqlite3.connect(file)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS ENTRY_DATA
                (   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Date TEXT,
                    Name TEXT,
                    Address TEXT,
                    Phone TEXT,
                    Interests TEXT,
                    Remarks TEXT
                )""")
class entry_data:
    def __init__(self, name='', address='', Phone_Number='', Date_Of_Enquiry=date.today()):
        self.index = 0
        self.Date_Of_Enquiry = Date_Of_Enquiry
        self.name = name
        self.address = address
        self.Phone_Number = Phone_Number
        self.Area_of_Interest = ''
        self.Remarks = ''

    def push(self, name, address, Phone_Number, Area_of_Interest, Remarks, Date_Of_Enquiry=date.today(),):
        self.Date_Of_Enquiry = Date_Of_Enquiry
        self.name = name
        self.address = address
        self.Phone_Number = Phone_Number
        self.Area_of_Interest = Area_of_Interest
        self.Remarks = Remarks

    def push_rem(self, Area_of_Interest, Remarks):
        self.Area_of_Interest = Area_of_Interest
        self.Remarks = Remarks

    def setIndex(self, id):
        self.index = id 
    
    def getName(self):
        return self.name
    def getIndex(self):
        return self.index 

def details(info_obj):
    print("*********************************")
    print("The details are as info")
    print('ID',info_obj.getIndex())
    print("Name:", info_obj.name)
    print("Address:", info_obj.address)
    print("List of Phone Numbers:", info_obj.Phone_Number)
    print("Area of interest:", info_obj.Area_of_Interest)
    date_ = date.strftime(info_obj.Date_Of_Enquiry, "%d/%m/%Y")
    print("Date:", date_)
    print("Remarks:", info_obj.Remarks)
    print("*********************************")


def push_data(info_obj):
    cur.execute("INSERT INTO ENTRY_DATA(Date, Name, Address, Phone, Interests, Remarks) VALUES(?,?,?,?,?,?)", (info_obj.Date_Of_Enquiry.strftime('%d/%m/%y'),
                                                               info_obj.name, info_obj.address, info_obj.Phone_Number, info_obj.Area_of_Interest, info_obj.Remarks))
    conn.commit()



def update_data(info_obj, index_param):
    cur.execute("SELECT * FROM ENTRY_DATA WHERE ID = ?",(index_param,))
    INDEX, date_temp, name, address, Phone_Number, Area_of_Interest, Remarks = cur.fetchone()
    date_obj = info_obj.Date_Of_Enquiry.strftime('%d/%m/%y')
    if date_obj != date_temp:
        update('Date',date_obj,index_param )
    if info_obj.name != name:
        update('Name',info_obj.name,index_param)
    if info_obj.address != address:
        update('Address',info_obj.address,index_param)
    if info_obj.Phone_Number!= Phone_Number:
        update('Phone',info_obj.Phone_Number,index_param)
    if info_obj.Area_of_Interest != Area_of_Interest:
        update('Interests',info_obj.Area_of_Interest,index_param)
    if info_obj.Remarks != Remarks:
        update('Remarks',info_obj.Area_of_Interest,index_param)

def update(var, val, index):
    cur.execute('UPDATE ENTRY_DATA SET '+ var + '= ? WHERE ID = ?',(val,index))
    conn.commit()

def delete(index):
    cur.execute("DELETE FROM ENTRY_DATA WHERE ID = ?",(index,))
    conn.commit()

def __get_data():
    # cur.execute("SELECT * FROM ENTRY_DATA")
    conn.commit()
    values = []
    for immediate_data in cur.fetchall():
        INDEX, date_temp, name, address, Phone_Number, Area_of_Interest, Remarks = immediate_data

        obj = entry_data(name, address, Phone_Number,
                         datetime.strptime(date_temp, '%d/%m/%y').date())
        obj.push_rem(Area_of_Interest, Remarks)
        obj.setIndex(INDEX)
        values.append(obj)
    return values

def get_all():
    cur.execute("SELECT * FROM ENTRY_DATA")
    return __get_data()

def get_data_by_datename(DATE, NAME=''):
    if NAME != '':
        cur.execute("SELECT * FROM ENTRY_DATA WHERE Date=? AND Name=?",
                    (DATE.strftime('%d/%m/%y'), NAME))
    else:
        cur.execute("SELECT * FROM ENTRY_DATA WHERE Date=?",
                    (DATE.strftime('%d/%m/%y'),))

    return __get_data()

def get_data_by_name(NAME):
    cur.execute("SELECT * FROM ENTRY_DATA WHERE Name LIKE ?",('%'+NAME+'%',))
    return __get_data()



def show_all():
    values = get_all()
    for x in values:
        details(x)
if __name__ == "__main__":
    show_all()
