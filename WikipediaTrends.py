from mwviews.api import PageviewsClient
import pandas as pd

p = PageviewsClient(user_agent='all-agents')

x = (p.article_views('en.wikipedia', ['Reliance Industries'], granularity='daily', start='20150701', end='20180318'))

df = pd.DataFrame()
df1 = pd.DataFrame()
Y = pd.read_csv("FinalData.csv")

timeslot = []
for date in x:
    items = x[date].items()
    timeslot.append({date : value for (timeslot, value) in items})
Date=[]
PageViews = []
for i in timeslot:
    for x, y in i.items():
        Date.append(x.date())
        PageViews.append(y)
#print(Date)
#print(PageViews)

df = pd.DataFrame(Date, columns=['Date'])
df1 = pd.DataFrame(PageViews, columns=['WikiPageViews'] )

df = df.merge(df1,left_index=True,right_index=True)

Y['Date']=pd.to_datetime(Y.Date)
df['Date']=pd.to_datetime(df.Date)
df = df.merge(Y, how ='right', on = 'Date') 
df.to_csv("FinalData.csv")