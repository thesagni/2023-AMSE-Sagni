import pandas as pd 
import re

url = 'https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv'
cols = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]
columns = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']

df = pd.read_csv(url, sep=';', encoding="latin1", header=None, skiprows=7, skipfooter=4,
                 usecols=cols, names=columns, engine='python')


df = df[df['petrol'].apply(lambda x: not re.search(r'-', str(x)))]
df = df[df['CIN'].apply(lambda x: re.match(r'^\d{5}$', str(x)) is not None)]


# Convert data types
data_types = {'petrol':'int64', 'diesel':'int64', 'gas':'int64', 'electro':'int64', 'hybrid':'int64', 'plugInHybrid':'int64', 'others':'int64'}
df = df.astype(data_types)
# Convert CIN column to string type
df['CIN'] = df['CIN'].astype(str)



# Write data to SQLite database
df.to_sql('cars', 'sqlite:///cars.sqlite', if_exists='replace', index=False)
