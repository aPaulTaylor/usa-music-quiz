import os
import pandas as pd
import re

#all_charts=pd.DataFrame()

#for fn in os.listdir('charts-data'):
#    top_100 = pd.read_csv('charts-data/'+fn)
#    top_100['week']=fn.split('.')[0][7:]
#    all_charts = all_charts.append(top_100)

#all_charts.to_csv('charts-data/all-singles-charts.csv',index=False)

all_charts=pd.read_csv('charts-data/all-singles-charts.csv')

def sanitize_title(title):
    title = re.sub('\(.*\)','',title)
    title = re.sub('[^A-Za-z0_9\s]','',title)
    title = title.strip()
    return title

all_charts['sanitized_title'] = all_charts.apply(lambda row: sanitize_title(row['titles']), axis=1)
print(all_charts.head(10))