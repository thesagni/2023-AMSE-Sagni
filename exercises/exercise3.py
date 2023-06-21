import pandas as pd 

url = 'https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv'
cols = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]
columns = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']

df = pd.read_csv(url, sep=';', encoding="latin1", header=None, skiprows=7, skipfooter=4,
                 usecols=cols, names=columns, engine='python',
                 converters={'CIN': str})


# Convert CIN column to string type
df['CIN'] = df['petrol'].astype(str)

# Replace '-' values with NaN
df = df.replace('-', float('nan'))


# Convert data types
data_types = {'petrol': 'float64', 'diesel': 'float64', 'gas': 'float64', 'electro': 'float64',
              'hybrid': 'float64', 'plugInHybrid': 'float64', 'others': 'float64'}
df = df.astype(data_types, copy=False)



# Write data to SQLite database
df.to_sql('cars', 'sqlite:///cars.sqlite', if_exists='replace', index=False)
