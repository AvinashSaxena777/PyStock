# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 01:12:26 2018

@author: Avinash
"""
import pandas as pd
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)
Y = pd.read_csv("RelianceYahoo1.csv")
X = Y['Date'].to_frame()
print(X['Date'])

df = pd.DataFrame()
x = pd.DataFrame()
final = []
kw_list = ["Reliance","Jio"]
i=0
while ( i < len(X) ):
    if(i>len(X)-90):
        print(str(X['Date'].iloc[i])+' '+str(X['Date'].iloc[-1]))
        pytrends.build_payload(kw_list, cat=0, timeframe=str(X['Date'].iloc[i])+' '+str(X['Date'].iloc[-1]), geo='', gprop='')
        i=i+91
        x=pytrends.interest_over_time()
        x['Date']=x.index
        df=df.append(x, ignore_index= True)
    else:
        print(str(X['Date'].iloc[i])+' '+str(X['Date'].iloc[i+90]))
        pytrends.build_payload(kw_list, cat=0, timeframe=str(X['Date'].iloc[i])+' '+str(X['Date'].iloc[i+90]), geo='', gprop='')
        i=i+91
        x=pytrends.interest_over_time()
        x['Date']=x.index
        df=df.append(x, ignore_index= True)

Y['Date']=pd.to_datetime(Y.Date)
df['Date']=pd.to_datetime(df.Date)
df = df.merge(Y, how ='right', on = 'Date')
df = df.drop(['isPartial'], axis =1)  
df.to_csv('FinalData.csv')
