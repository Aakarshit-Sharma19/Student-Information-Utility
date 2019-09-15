from datetime import date, datetime
import sqlite3
# To be Run everytime this module is used
conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS ENTRY_DATA
                (
                    Date TEXT,
                    Name TEXT,
                    Address TEXT,
                    Phone TEXT,
                    Interests TEXT,
                    Remarks TEXT
                )""")


class entry_data:
    def __init__(self, name='', address='', Phone_Number='', Date_Of_Enquiry=date.today()):
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


def details(info1):
    print("The details are as info")
    print("Name:", info1.name)
    print("Address:", info1.address)
    print("List of Phone Numbers:", info1.Phone_Number)
    print("Area of interest:", info1.Area_of_Interest)
    date_ = date.strftime(info1.Date_Of_Enquiry, "%d/%m/%Y")
    print("Date:", date_)
    print("Remarks:", info1.Remarks)


def push_data(info_obj):
    cur.execute("INSERT INTO ENTRY_DATA VALUES(?,?,?,?,?,?)", (info_obj.Date_Of_Enquiry.strftime('%d/%m/%y'),
                                                               info_obj.name, info_obj.address, info_obj.Phone_Number, info_obj.Area_of_Interest, info_obj.Remarks))
    conn.commit()


def get_data():
    # cur.execute("SELECT * FROM ENTRY_DATA")
    conn.commit()
    values = []
    for immediate_data in cur.fetchall():
        date_temp, name, address, Phone_Number, Area_of_Interest, Remarks = immediate_data

        obj = entry_data(name, address, Phone_Number,
                         datetime.strptime(date_temp, '%d/%m/%y').date())
        obj.push_rem(Area_of_Interest, Remarks)
        values.append(obj)
    return values


def get_all():
    cur.execute("SELECT * FROM ENTRY_DATA")
    return get_data()


def get_data_by_datename(DATE, NAME=''):
    if NAME != '':
        cur.execute("SELECT * FROM ENTRY_DATA WHERE Date=? AND Name=?",
                    (DATE.strftime('%d/%m/%y'), NAME))
    else:
        cur.execute("SELECT * FROM ENTRY_DATA WHERE Date=?",
                    (DATE.strftime('%d/%m/%y'),))

    return get_data()
def show_all():
    values = get_all()
    for x in values:
        details(x)
