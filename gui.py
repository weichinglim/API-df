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
root.geometry("2000x2000")

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.grid(column=2,row=0)
canvas.draw()

today = date.today()
# today.place(x=0, y=0)

# Add Calendar
cal = Calendar(root, selectmode='day',
               year=2020, month=5,
               day=22)
cal.grid(column=0, row=0)


def button_click():
    date.config(text="Selected Date is: " + cal.get_date())
    canvas.draw()



# Add Button and Label
btn = Button(root, text="Get Date",
       command=button_click)

btn.grid(column=1, row=0)

date = Label(root, text="")
date.grid(column=0, row=1)


types = ['range', 'date']
chosen = ttk.Combobox(root, values=types, width=7)
chosen.grid(column=0, row=2)

# Execute Tkinter
root.mainloop()
