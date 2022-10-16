from tkinter import *
from tkcalendar import Calendar

window = Tk()

window.title("Welcome to LikeGeeks app")

# Add Calendar
cal = Calendar(window, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)


def grad_date():
    date.config(text="Selected Date is: " + cal.get_date())


# Add Button and Label
Button(window, text="Get Date", command=grad_date).pack(pady=20)

date = Label(window, text = "")
date.pack(pady = 20)

window.mainloop()