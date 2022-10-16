import api_ele
import pandas as pd

def new_data(data1,data2):
    new = pd.merge(data1,data2,on='date')
    return new

def co2_em(data):
    green_gas = pd.DataFrame()
    green_gas['date'] = data['date']
    green_gas['gas_co2'] = (data['main_gas']+data['oak_gas'])*1000*data['gas_the']*data['gas_co2'] 
    green_gas['pellet_co2'] = (data['pellet']+data['pellet_coal']*data['pellet_per'])*0.5*data['pellet_the']*data['pellet_co2']
    green_gas['coal_co2'] = (data['pellet_coal']*(1-data['pellet_per']))*0.5*data['coal_the']*data['coal_co2']
    green_gas['hull_co2'] = (data['oat_hull'])*0.5*data['hull_the']*data['hull_co2']
    green_gas['electric_co2'] = ((data['main_ele']+data['oak_ele'])*data['ele_col_fac']*data['val coal']+(data['main_ele']+data['oak_ele'])*data['ele_nat_fac']*data['val natGas'])*1000
    return green_gas

def electric_type():
    request_Wind = 'https://api.eia.gov/series/?api_key=wrLV2rktOe2MS5qzsVy8sFhs6ghNnDKt2lcPef0K&series_id=EBA.MISO-ALL.NG.WND.H&start=20210701T14Z'
    nameW = "wind"
    dfW = api_ele.get_api(request_Wind, nameW)
    aggW = api_ele.agg_date(dfW)
    # Solar API
    request_Solar = 'https://api.eia.gov/series/?api_key=wrLV2rktOe2MS5qzsVy8sFhs6ghNnDKt2lcPef0K&series_id=EBA.MISO-ALL.NG.SUN.H&start=20210701T14Z'
    nameS = "solar"
    dfS = api_ele.get_api(request_Solar, nameS)
    aggS = api_ele.agg_date(dfS)
    # HydroGen API
    request_Hydro = 'https://api.eia.gov/series/?api_key=wrLV2rktOe2MS5qzsVy8sFhs6ghNnDKt2lcPef0K&series_id=EBA.MISO-ALL.NG.WAT.H&start=20210701T14Z'
    nameH = "hydro"
    dfH = api_ele.get_api(request_Hydro, nameH)
    aggH = api_ele.agg_date(dfH)
    # CoalGen API
    request_Coal = 'https://api.eia.gov/series/?api_key=wrLV2rktOe2MS5qzsVy8sFhs6ghNnDKt2lcPef0K&series_id=EBA.MISO-ALL.NG.COL.H&start=20210701T14Z'
    nameC = "coal"
    dfC = api_ele.get_api(request_Coal, nameC)
    aggC = api_ele.agg_date(dfC)
    # Natural Ges Gen API
    request_NatGas = 'https://api.eia.gov/series/?api_key=wrLV2rktOe2MS5qzsVy8sFhs6ghNnDKt2lcPef0K&series_id=EBA.MISO-ALL.NG.NG.H&start=20210701T14Z'
    nameNG = "natGas"
    dfNat = api_ele.get_api(request_NatGas, nameNG)
    aggNat = api_ele.agg_date(dfNat)    
    # Nuclear API
    request_Nuclear = 'https://api.eia.gov/series/?api_key=wrLV2rktOe2MS5qzsVy8sFhs6ghNnDKt2lcPef0K&series_id=EBA.MISO-ALL.NG.NUC.H&start=20210701T14Z'
    nameNu = "nuclear"
    dfNu = api_ele.get_api(request_Nuclear, nameNu)
    aggNu = api_ele.agg_date(dfNu)  
    ele_all = new_data(new_data(new_data(new_data(new_data(aggW,aggS),aggH),aggC),aggNat),aggNu)
    ele_all = ele_all.div(ele_all.sum(axis=1), axis=0)[['val coal','val natGas']]
    ele = ele_all.loc[ele_all.index <= '2022-06-30']
    return ele

def histroy_energy(ele):
	energy = pd.read_csv('energy.csv', sep=',')
	energy["ele_col_fac"] = 2.23 * 0.453592
	energy["ele_nat_fac"] = 0.91*0.453592
	energy = new_data(energy,ele)
	return energy

