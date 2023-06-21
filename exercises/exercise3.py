
import pandas as pd 

url = 'https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv'
cols_sql = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]
columns = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro','hybrid', 'plugInHybrid', 'others']

df = pd.read_csv(url, sep=';', encoding="latin1", header=None, skiprows=7, skipfooter=4,
                 usecols=cols_sql, names=columns, engine='python',
                 converters={'CIN': str})

# Convert data types
data_types = {
    'date': 'TEXT',
    'CIN': 'TEXT',
    'name': 'TEXT',
    'petrol': 'INTEGER',
    'diesel': 'INTEGER',
    'gas': 'INTEGER',
    'electro': 'INTEGER',
    'hybrid': 'INTEGER',
    'plugInHybrid': 'INTEGER',
    'others': 'INTEGER'
}
df = df.astype(data_types)

df.to_sql('cars', 'sqlite:///cars.sqlite', if_exists='replace', index=False)
