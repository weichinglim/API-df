import datetime as dt
import time
import requests
import pandas as pd

def agg_date(df):
    dt_frame = df
    test_W = dt_frame.groupby(['date']).sum()  
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
    df['date'] = t
    
    colName = "val " + name
    df[colName] = val
    
    df['date'] = pd.to_datetime(df['date'], format = '%Y%m%d').dt.strftime("%Y-%m-%d")
    return df