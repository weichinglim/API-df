#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 18:48:47 2022

@author: limweiching
"""

import requests
import pandas as pd


r = requests.get('https://api.eia.gov/series/?api_key=wrLV2rktOe2MS5qzsVy8sFhs6ghNnDKt2lcPef0K&series_id=EBA.MISO-ALL.NG.WND.H&start=20220816T14Z')
# data_text = str(data)
data = r.json()

# print(data['series'][0]['data'])

all = data['series'][0]['data']
print(all)




# df = pd.DataFrame({'Time':all[], 'Val':})

# print(df)

for i in all:
    timestamp = i[0]
    value = i[1]
    df = pd.DataFrame({'Time':timestamp, 'Val':value})
    

