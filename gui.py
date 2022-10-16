from tkinter import *
from tkcalendar import Calendar
from datetime import date
# import tkFont


window = Tk()

# Add background color
# window['background']='#87CEFF' # skyblue1:https://www.webucator.com/article/python-color-constants-module/

window.title('Real-time Dashboard') #, font=(18,'Arial'))
# window.configure(font = ("Comic Sans MS", 20, "bold")) #Arial
Title = Label(text="Campus CO2 Emission Profile")
Title.pack()
Title.configure(font = ("Comic Sans MS", 20, "bold")) #Arial
window.geometry('920x640')

today = date.today()
# today.place(x=0, y=0)

# Add Calendar
cal = Calendar(window, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)


def grad_date():
    date.config(text="Selected Date is: " + cal.get_date())


# Add Button and Label
Button(window, text="Get Date", command=grad_date).pack() # ipadx=20, ipady=10) # pady=50)
date = Label(window, text = "")
date.place(x=5, y=0) #pack() # ipadx=50) #pady = 50)

Button(window, text="Refresh").pack()

# Real-time Auto Refresh




window.mainloop()