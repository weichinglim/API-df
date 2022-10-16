import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def co2_em_day(data,time):
    try:
        pan = data.loc[data['date'] == time].drop(['date'],axis=1).iloc[0]
    except:
        print("Invalid input")
    f = pan.plot.pie(subplots=False,title="CO2 Emission of Different Sources", shadow=True ,autopct='%1.1f%%',legend=True,ylabel='', labeldistance=None)
    fig = f.get_figure()
    f.legend(['Natural Gas', 'Pellets', 'Coal', 'Oat Hulls','Electric'],bbox_to_anchor=(1, 1.02), loc='upper left')
    return fig

def co2_em_history(data,time):
    if time=='full':
        f = data.plot()
    else:
        time1 = time[0]
        time2 = time[1]
    time_range = (data['date'] > time1) & (data['date'] <= time2)
    data = data.loc[time_range]
    data = data.set_index('date')
    f = data.plot(title="CO2 Emission of Different Sources",legend=True)
    f.set_xticklabels(f.xaxis.get_majorticklabels(), rotation=45)
    fig = f.get_figure()
    f.legend(['Natural Gas', 'Pellets', 'Coal', 'Oat Hulls','Electric'],bbox_to_anchor=(1, 1.02), loc='upper left')
    return fig