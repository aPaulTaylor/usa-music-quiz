import os
import pandas as pd
import re
import datetime

#all_charts=pd.DataFrame()

#for fn in os.listdir('charts-data'):
#    if 'top100' in fn:
#        top_100 = pd.read_csv('charts-data/'+fn)
#        top_100['week']=fn.split('.')[0][7:]
#        all_charts = all_charts.append(top_100)

all_charts.to_csv('charts-data/all-singles-charts.csv',index=False)

all_charts=pd.read_csv('charts-data/all-singles-charts.csv')

def sanitize_title(title):
    title = re.sub('\(.*\)','',title)
    title = re.sub('{.*}', '', title)
    title = re.sub('[^A-Za-z0-9\s]','',title)
    title = title.strip()
    return title

all_charts['sanitized_title'] = all_charts.apply(lambda row: sanitize_title(row['titles']), axis=1)
all_charts['title_signature'] = all_charts.apply(lambda row: tuple(map(len,row['sanitized_title'].split(' '))), axis=1)
all_charts['week_commencing'] = all_charts.apply(lambda row: datetime.datetime.strptime(row['week'], "%d %B %Y") , axis=1)

all_charts['sanitized_title'][(all_charts['title_signature']==(5,5)) & (all_charts['positions']<41)].nunique()

top40_songs=all_charts[(all_charts['positions']<41)].groupby(['artists','titles','sanitized_title','title_signature']).agg({'positions':min,'week_commencing':min})
top40_songs.reset_index(inplace=True)
top40_songs.columns=['artist','title','sanitized_title','title_signature','top_position','first_week']
top40_songs.to_csv('charts-data/top_40_songs.csv',index=False)