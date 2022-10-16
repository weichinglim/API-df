from tkinter import *
from tkcalendar import Calendar
# import tkFont


window = Tk()

window.title('Campus CO2 Emission Profile') #, font=(18,'Arial'))
Title = Label(text="Campus CO2 Emission Profile")
Title.pack()
Title.configure(font = ("Comic Sans MS", 20, "bold")) #Arial
window.geometry('920x640')

# Add Calendar
cal = Calendar(window, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)


def grad_date():
    date.config(text="Selected Date is: " + cal.get_date())


# Add Button and Label
Button(window, text="Get Date", command=grad_date).pack(pady=20)

Button(window, text="Refresh").pack()

# Real-time Auto Refresh


date = Label(window, text = "")
date.pack(pady = 20)

window.mainloop()