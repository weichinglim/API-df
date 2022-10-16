from tkinter import *
from tkcalendar import Calendar
from datetime import date
# import tkFont
from tkinter import ttk
import pandas as pd
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)





# Create Object
root = Tk()

# Set geometry
root.geometry("1000x600")

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().place(anchor=E, x=980, y=300, relheight=0.4, relwidth=0.4)

today = date.today()
# today.place(x=0, y=0)

# Add Calendar
cal = Calendar(root, selectmode='day',
               year=2020, month=5,
               day=22)
cal.place(anchor=NW, x=20, y=10, relheight=0.3, relwidth=0.3)

def button_click(): 
    date.config(text="Selected Date is: " + cal.get_date())
    canvas.draw()

# Add Button and Label
btn = Button(root, text="Confirm/Refresh",
       command=button_click)

btn.place(anchor=NW, x=20, y=220, relheight=0.05, relwidth=0.1)

range1 = Label(root, text="")
range1.place(anchor=NW, x=20, y=350, relheight=0.05, relwidth=0.15)

range2 = Label(root, text="")
range2.place(anchor=NW, x=130, y=350, relheight=0.05, relwidth=0.15)

def button_click_range1():
    range1.config(text= cal.get_date())

def button_click_range2():
    range2.config(text= cal.get_date())


btn_range1 = Button(root, text="RangeStart", command=button_click_range1)
btn_range1.place(anchor=NW, x=20, y=390, relheight=0.05, relwidth=0.10)

btn_range2 = Button(root, text="RangeEnd", command=button_click_range2)
btn_range2.place(anchor=NW, x=130, y=390, relheight=0.05, relwidth=0.10)


date = Label(root, text="")
date.place(anchor=NW, x=20, y=500, relheight=0.05, relwidth=0.2)


types = ['range', 'date']
chosen = ttk.Combobox(root, values=types, width=7)
chosen.place(anchor=NW, x=20, y=300, relheight=0.05, relwidth=0.1)

# Execute Tkinter
root.mainloop()