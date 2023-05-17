import pandas as pd
#downloading 1st data souce

df = pd.read_csv('https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-01.csv',sep=',') 
df = pd.read_csv('https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-02.csv',sep=',') 
df = pd.read_csv('https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-03.csv',sep=',') 
df = pd.read_csv('https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-04.csv',sep=',') 
df = pd.read_csv('https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-05.csv',sep=',') 
df = pd.read_csv('https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-06.csv',sep=',') 
df = pd.read_csv('https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-07.csv',sep=',') 
df = pd.read_csv('https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-08.csv',sep=',') 
df = pd.read_csv('https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-09.csv',sep=',') 
df = pd.read_csv('https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-10.csv',sep=',') 
df = pd.read_csv('https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-11.csv',sep=',') 
df = pd.read_csv('https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-12.csv',sep=',') 

df.columns.value[0]= 'Total Bicylce count'


#downloading 2nd data souce
#data source- https://www-genesis.destatis.de/genesis/online?language=en&sequenz=statistikTabellen&selectionname=46241#abreadcrumb

df = pd.read_csv('C:/Users/reham/Desktop/subj sem 4/AMSE(DATA ENGG)/data/data source 2/AccidentData.csv',sep=',') 

#renaming needed rows :
df.rows.value[24] = 'Total Accidents - Inside built-up areas'
df.rows.value[25] = 'Total Accidents - Outside built-up areas'
df.rows.value[26] = 'Total Accidents - On motorways/freeways'

#saving table to sqlite file
df.to_sql('Bicycle_Accidents','sqlite:///Bicycle_data.sqlite', if_exists='replace', index=False)
