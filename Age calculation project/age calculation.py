# import all functions from the tkinter
from tkinter import *
from PIL import Image, ImageTk
# import messagebox class from tkinter
from tkinter import messagebox
import tkinter as tk
import mysql.connector
# from common_util import *
import sqlalchemy
import pymysql.cursors
# import quote

# Function for clearing the
# contents of all text entry boxes
def get_connection_engine_local():
    # return sqlalchemy.create_engine('mysql+pymysql://bfcm:%s@localhost/bfcm' % quote('Iswarya23'), pool_pre_ping=True)
    return sqlalchemy.create_engine('mysql+pymysql://root:preeash9360@localhost:3306/calcutor')
def get_connection_localDB():
    connection = pymysql.connect(host='localhost',
    user='root',
    password='preeash9360',
    port=3306,
    db='calcutor',
    charset='utf8',
    local_infile=True,
    cursorclass=pymysql.cursors.DictCursor)
    return connection

def clearAll() :
    # deleting the content from the entry box
    dayField.delete(0, END)
    monthField.delete(0, END) 
    yearField.delete(0, END)
    givenDayField.delete(0, END)
    givenMonthField.delete(0, END)
    givenYearField.delete(0, END)
    rsltDayField.delete(0, END)
    rsltMonthField.delete(0, END)
    rsltYearField.delete(0, END)
# function for checking error
def checkError():
    # if any of the entry field is empty
    # then show an error message and clear
    # all the entries
    if (dayField.get() == "" or monthField.get() == ""
            or yearField.get() == "" or givenDayField.get() == ""
            or givenMonthField.get() == "" or givenYearField.get() == ""):
        # show the error message
        messagebox.showerror("Input Error")
        # clearAll function calling
        clearAll()
        return -1
# function to calculate Age
def calculateAge():
    # check for error
    value = checkError()
    # if error is occur then return
    if value == -1:
        return
    else:
        # take a value from the respective entry boxes
        # get method returns current text as string
        birth_day = int(dayField.get())
        birth_month = int(monthField.get())
        birth_year = int(yearField.get())

        given_day = int(givenDayField.get())
        given_month = int(givenMonthField.get())
        given_year = int(givenYearField.get())

        # if birth date is greater then given birth_month
        # then donot count this month and add 30 to the date so
        # as to subtract the date and get the remaining days
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (birth_day > given_day):
            # import pdb;pdb.set_trace()
            given_month = given_month - 1
            given_day = given_day + month[birth_month - 1]
            # if birth month exceeds given month, then
        # donot count this year and add 12 to the
        # month so that we can subtract and find out
        # the difference
        if (birth_month > given_month):
            given_year = given_year - 1
            given_month = given_month + 12
        # calculate day, month, year
        calculated_day = given_day - birth_day;
        calculated_month = given_month - birth_month;
        calculated_year = given_year - birth_year;
        # calculated day, month, year write back
        # to the respective entry boxes
        # import pdb;
        # pdb.set_trace()
        print(calculated_day)
        print(calculated_month)
        print(calculated_year)

        connection = get_connection_localDB()
        cursor = connection.cursor()
        # Insert data into the table
        # sql = """INSERT INTO personal (name, email) VALUES ("""+name+","+email+")"""
        # sql="""INSERT INTO personal (name, email) VALUES ('""" + name + """','""" + email + """') """
        sql = "INSERT INTO cal (year,month,days) VALUES (%s, %s, %s)"
        val = (calculated_year, calculated_month, calculated_day)
        cursor.execute(sql, val)
        # cursor.execute(sql)
        connection.commit()
        # messagebox.showinfo("Success", "Data saved successfully")

        # year = rsltYearField_entry.get()
        # month = rsltMonthField_entry.get()
        # days = rsltDayField_entry.get()

        # insert method inserting the
        # value in the text entry box.

        rsltDayField.insert(10, str(calculated_day))
        rsltMonthField.insert(10, str(calculated_month))
        rsltYearField.insert(10, str(calculated_year))

    # Driver Code
if __name__ == "__main__":
    # Create a GUI window
    gui = Tk()
    # Set the background colour of GUI window
    gui.configure(background="#194157")
    # set the name of tkinter GUI window
    gui.title("Age Calculator")
    # Set the configuration of GUI window
    gui.geometry("525x260")
    # Load the background image
    background_image_path = "D:\\image\\moon.jpg"   # Replace "background_image.jpg" with the path to your image file
    background_image = Image.open(background_image_path)

    # Resize the background image to fit the window size
    window_width = gui.winfo_screenwidth()
    window_height = gui.winfo_screenheight()
    background_image = background_image.resize((window_width, window_height))

    # Convert the background image to Tkinter format
    tk_background_image = ImageTk.PhotoImage(background_image)

    # Create a label to display the background image
    background_label = tk.Label(gui, image=tk_background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # image_path = "D:\\image\\moon.jpg"  # Replace "logo.png" with the path to your image file
    # image = Image.open(image_path)
    #  # Resize the image if needed
    # image = image.resize((200, 200))
    # Convert the image to Tkinter format
    # tk_image = ImageTk.PhotoImage(image)
    #
    # # Create a label to display the image
    # image_label = tk.Label(gui, image=tk_image)
    # image_label.grid(row=0,column=0)


    dob = Label(gui, text="Date Of Birth", bg="#733464")

    # Create a Given Date : label
    givenDate = Label(gui, text="Given Date", bg="#733464")

    # Create a Day : label
    day = Label(gui, text="Day", bg="#194157")


    # Create a Month : label
    month = Label(gui, text="Month", bg="#194157")

    # Create a Year : label
    year = Label(gui, text="Year", bg="#194157")

    # Create a Given Day : label
    givenDay = Label(gui, text="Given Day", bg="#194157")

    # Create a Given Month : label
    givenMonth = Label(gui, text="Given Month", bg="#194157")

    # Create a Given Year : label
    givenYear = Label(gui, text="Given Year", bg="#194157")

    # Create a Years : label
    rsltYear = Label(gui, text="Years", bg="#194157")

    # Create a Months : label
    rsltMonth = Label(gui, text="Months", bg="#194157")

    # Create a Days : label
    rsltDay = Label(gui, text="Days", bg="#194157")

    # Create a Resultant Age Button and attached to calculateAge function
    resultantAge = Button(gui, text="Resultant Age", fg="Black", bg="#733464", command=calculateAge)

    # Create a Clear All Button and attached to clearAll function
    clearAllEntry = Button(gui, text="Clear All", fg="Black", bg="#733464", command=clearAll)

    # Create a text entry box for filling or typing the information.
    dayField = Entry(gui)
    monthField = Entry(gui)
    yearField = Entry(gui)
    givenDayField = Entry(gui)
    givenMonthField = Entry(gui)
    givenYearField = Entry(gui)

    rsltYearField = Entry(gui)
    rsltMonthField = Entry(gui)
    rsltDayField = Entry(gui)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    dob.grid(row=0, column=1)

    day.grid(row=1, column=0)
    dayField.grid(row=1, column=1)

    month.grid(row=2, column=0)
    monthField.grid(row=2, column=1)

    year.grid(row=3, column=0)
    yearField.grid(row=3, column=1)

    givenDate.grid(row=0, column=4)

    givenDay.grid(row=1, column=3)
    givenDayField.grid(row=1, column=4)

    givenMonth.grid(row=2, column=3)
    givenMonthField.grid(row=2, column=4)

    givenYear.grid(row=3, column=3)
    givenYearField.grid(row=3, column=4)

    resultantAge.grid(row=4, column=2)

    rsltYear.grid(row=5, column=2)
    rsltYearField.grid(row=6, column=2)

    rsltMonth.grid(row=7, column=2)
    rsltMonthField.grid(row=8, column=2)

    rsltDay.grid(row=9, column=2)
    rsltDayField.grid(row=10, column=2)

    clearAllEntry.grid(row=12, column=2)

# save_button = Button(gui, text="Save", command=save_data)
# save_button.grid(row=15, column=2)


    # Start the GUI
gui.mainloop()
