import data_clear.py
import figure.py


ele = data_clear.electric_type()
energy = data_clear.histroy_energy(ele)
co2 = data_clear.co2_em(energy)
f1 = figure.co2_em_day(co2,date)
f2 = figure.co2_em_history(co2,datelist)