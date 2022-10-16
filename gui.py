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
cal.place(anchor=NW, x=20, y=10, relheight=0.2, relwidth=0.2)


def button_click():
    date.config(text="Selected Date is: " + cal.get_date())
    canvas.draw()



# Add Button and Label
btn = Button(root, text="Get Date",
       command=button_click)

btn.place(anchor=NW, x=20, y=135, relheight=0.05, relwidth=0.1)

date = Label(root, text="")
date.place(anchor=NW, x=20, y=280, relheight=0.05, relwidth=0.2)


types = ['range', 'date']
chosen = ttk.Combobox(root, values=types, width=7)
chosen.place(anchor=NW, x=20, y=200, relheight=0.05, relwidth=0.1)

# Execute Tkinter
root.mainloop()