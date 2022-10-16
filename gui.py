from tkinter import *
from tkcalendar import Calendar
from datetime import date
# import tkFont
from tkinter import ttk

# Create Object
root = Tk()

# Set geometry
root.geometry("2000x2000")

today = date.today()
# today.place(x=0, y=0)

# Add Calendar
cal = Calendar(root, selectmode='day',
               year=2020, month=5,
               day=22)
cal.grid(column=0, row=0)


def grad_date():
    date.config(text="Selected Date is: " + cal.get_date())


# Add Button and Label
btn = Button(root, text="Get Date",
       command=grad_date)

btn.grid(column=1, row=0)

date = Label(root, text="")
date.grid(column=0, row=1)


types = ['range', 'date']
chosen = ttk.Combobox(root, values=types, width=7)
chosen.grid(column=0, row=2)

# Execute Tkinter
root.mainloop()
