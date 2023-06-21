
import pandas as pd 

url = 'https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv'
cols_sql = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]
columns = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro','hybrid', 'plugInHybrid', 'others']

df = pd.read_csv(url, sep=';', encoding="latin1", header=None, skiprows=7, skipfooter=4,
                 usecols=cols_sql, names=columns, engine='python',
                 converters={'CIN': str})

# Convert data types
df = df[df["petrol"].str.contains("-")==False]
data_types = {'petrol':'int64', 'diesel':'int64', 'gas':'int64', 'electro':'int64', 'hybrid':'int64', 'plugInHybrid':'int64', 'others':'int64'}
df = df.astype(data_types)

df.to_sql('cars', 'sqlite:///cars.sqlite', if_exists='replace', index=False)
