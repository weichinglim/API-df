from tkinter import *
from tkcalendar import Calendar
from datetime import date
import datetime
# import tkFont
from tkinter import ttk
import pandas as pd
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import data_clear
import figure



ele = data_clear.electric_type()
energy = data_clear.histroy_energy(ele)
co2 = data_clear.co2_em(energy)


# Create Object
root = Tk()

# Set geometry
root.geometry("1280x600")

fig = Figure(figsize=(5, 4), dpi=100)
# canvas = FigureCanvasTkAgg(fig, master=root)
# canvas.get_tk_widget().place(anchor=E, x=980, y=300, relheight=0.4, relwidth=0.4)
# fig = figure.co2_em_day(co2,"2022-05-01")

# t = np.arange(0, 3, .01)
# fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

# canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
# canvas.draw()
# canvas.get_tk_widget().place(anchor=E, x=980, y=300, relheight=0.4, relwidth=0.4)

# today = date.today()
# today.place(x=0, y=0)

# Add Calendar
cal = Calendar(root, selectmode='day',
               year=2022, month=5,
               day=22)
cal.place(anchor=NW, x=20, y=10, relheight=0.3, relwidth=0.25)

def button_click(): 
    global fig
    # fig.clear()
    fig.clear()
    
    if chosen.get() == 'range':
        range_start = datetime.datetime.strptime(range_1, "%m/%d/%y").strftime("20%y-%m-%d")
        range_end = datetime.datetime.strptime(range_2, "%m/%d/%y").strftime("20%y-%m-%d")
        time_input = [range_start, range_end]
        fig = figure.co2_em_history(co2, time_input)
        
    elif chosen.get() == 'date':
        # global canvas
        # canvas.delete("all")
        # fig.clear()
        # date.config(text="Selected Date is: " + cal.get_date())
        co2_time = datetime.datetime.strptime(cal.get_date(), "%m/%d/%y").strftime("20%y-%m-%d")
        date.config(text="Selected Date is: " + co2_time)
        fig = figure.co2_em_day(co2,co2_time)
        print(type(fig))
        
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().place(anchor=E, x=1260, y=300, relheight=0.8, relwidth=0.7)
    # canvas.get_tk_widget().place(x=300, y=100, width =800, height=400)
    

# Add Button and Label
btn = Button(root, text="Confirm/Refresh",
       command=button_click)

btn.place(anchor=NW, x=20, y=220, relheight=0.05, relwidth=0.1)

range1 = Label(root, text="")
range1.place(anchor=NW, x=20, y=350, relheight=0.05, relwidth=0.1)

range2 = Label(root, text="")
range2.place(anchor=NW, x=130, y=350, relheight=0.05, relwidth=0.1)

range_1 = cal.get_date()
range_2 = cal.get_date()

def button_click_range1():
    range1.config(text= cal.get_date())
    global range_1
    range_1 = cal.get_date()
    
def button_click_range2():
    range2.config(text= cal.get_date())
    global range_2
    range_2 = cal.get_date()


btn_range1 = Button(root, text="RangeStart", command=button_click_range1)
btn_range1.place(anchor=NW, x=20, y=390, relheight=0.05, relwidth=0.10)

btn_range2 = Button(root, text="RangeEnd", command=button_click_range2)
btn_range2.place(anchor=NW, x=130, y=390, relheight=0.05, relwidth=0.10)


date = Label(root, text="")
date.place(anchor=NW, x=20, y=500, relheight=0.05, relwidth=0.2)


types = ['range', 'date']
chosen = ttk.Combobox(root, values=types, width=7)
chosen.current(0)
chosen.place(anchor=NW, x=20, y=300, relheight=0.05, relwidth=0.1)

#################################################################

# fig = figure.co2_em_day(co2,"2022-05-01")

# Execute Tkinter
root.mainloop()