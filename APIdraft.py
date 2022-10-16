# API-keys

import requests
import pandas as pd
import datetime as dt
import time

def agg_date(df):
    dt_frame = df
    test_W = dt_frame.groupby(['time']).sum()
    print('--Agg--')
    print(test_W)
    
    return test_W

def get_api(request_url, name):
    url = request_url
    r = requests.get(url)
    data = r.json()
    allData = data['series'][0]['data']
    
    df = pd.DataFrame()
    t = []
    val = []
    for i in allData:
        t.append(i[0][0:8])
        val.append(i[1])
    df['time'] = t
    
    colName = "val " + name
    df[colName] = val
    
    df['time'] = pd.to_datetime(df['time'], format = '%Y%m%d').dt.strftime("%Y-%m-%d")
    #print('--DF--')
    #print(df)
    
    return df
    
def main():

    # Wind API
    request_Wind = 'https://api.eia.gov/series/?api_key=s271BdyiPWCqLm1TgLpr81CsMPhFMwqnJ2QXKaDL&series_id=EBA.MISO-ALL.NG.WND.H&start=20210101T14Z'
    nameW = "wind"
    dfW = get_api(request_Wind, nameW)
    aggW = agg_date(dfW)
    
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
    # Solar API
    request_Solar = 'https://api.eia.gov/series/?api_key=s271BdyiPWCqLm1TgLpr81CsMPhFMwqnJ2QXKaDL&series_id=EBA.MISO-ALL.NG.SUN.H&start=20210101T14Z'
    nameS = "solar"
    dfS = get_api(request_Solar, nameS)
    aggS = agg_date(dfS)
    
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
    # HydroGen API
    request_Hydro = 'https://api.eia.gov/series/?api_key=s271BdyiPWCqLm1TgLpr81CsMPhFMwqnJ2QXKaDL&series_id=EBA.MISO-ALL.NG.WAT.H&start=20210101T14Z'
    nameH = "hydro"
    dfH = get_api(request_Hydro, nameH)
    aggH = agg_date(dfH)
    
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    # CoalGen API
    request_Coal = 'https://api.eia.gov/series/?api_key=s271BdyiPWCqLm1TgLpr81CsMPhFMwqnJ2QXKaDL&series_id=EBA.MISO-ALL.NG.COL.H&start=20220816T14Z'
    nameC = "coal"
    dfC = get_api(request_Coal, nameC)
    aggC = agg_date(dfC)
    
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
    # Natural Ges Gen API
    request_NatGas = 'https://api.eia.gov/series/?api_key=s271BdyiPWCqLm1TgLpr81CsMPhFMwqnJ2QXKaDL&series_id=EBA.MISO-ALL.NG.NG.H&start=20220816T14Z'
    nameNG = "natGas"
    dfNat = get_api(request_NatGas, nameNG)
    aggNat = agg_date(dfNat)    
    
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
    # Nuclear API
    request_Nuclear = 'https://api.eia.gov/series/?api_key=s271BdyiPWCqLm1TgLpr81CsMPhFMwqnJ2QXKaDL&series_id=EBA.MISO-ALL.NG.NUC.H&start=20220816T14Z'
    nameNu = "nuclear"
    dfNu = get_api(request_Nuclear, nameNu)
    aggNu = agg_date(dfNu)    
    

main()


