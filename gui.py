from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

# Add Calendar
cal = Calendar(root, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)


def grad_date():
    date.config(text="Selected Date is: " + cal.get_date())


# Add Button and Label
Button(root, text="Get Date", command=grad_date).pack(pady=20)

date = Label(root, text = "")
date.pack(pady = 20)

window.mainloop()