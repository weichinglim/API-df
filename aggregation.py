import data_clear
import figure


ele = data_clear.electric_type()
energy = data_clear.histroy_energy(ele)
co2 = data_clear.co2_em(energy)
figure.co2_em_day(co2,"2022-05-01")
