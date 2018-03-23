# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:29:02 2018

@author: Avinash
"""
#Packages Required

import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import requests


stock = "RELIANCE.NS"
terms = ["Reliance", "Jio"]
begin_date = "2015-07-01"
end_date = "2018-03-18"

#86GWLA2M8WL2J702
API_KEY = "86GWLA2M8WL2J702"
ts = TimeSeries(key=API_KEY)

print(ts.TIME_SERIES_DAILY_ADJUSTED(symbol = stock))


url = "https://www.alphavantage.co/query"

symbol = "RELIANCE.NS"
function = "TIME_SERIES_DAILY_ADJUSTED"
api_key = "86GWLA2M8WL2J702"

data = { "function": function, 
    "symbol": symbol,
     "outputsize": "full",
     "datatype": "csv",
     "apikey": api_key}

page = requests.get(url, params = data)

with open("test.csv", 'w') as oF:
    oF.write(page.text)
    
df_test = pd.read_csv("test.csv")
df_test.to_csv("test.csv")