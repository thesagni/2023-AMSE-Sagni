import pandas as pd 

url = 'https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv'
cols = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]
columns = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']

df = pd.read_csv(url, sep=';', encoding="iso-8859-1", header=None, skiprows=6, skipfooter=4,
                 usecols=cols, names=columns, engine='python', na_values='.', thousands=',' )

# Filter out rows with '-' in petrol column
df = df[~df['petrol'].str.contains('-', na=False)]

# Ensure 'CIN' column has exactly five characters
df = df[df['CIN'].str.len() == 5]

# Convert data types
data_types = {'petrol': 'int64', 'diesel': 'int64', 'gas': 'int64', 'electro': 'int64',
              'hybrid': 'int64', 'plugInHybrid': 'int64', 'others': 'int64'}
df = df.astype(data_types)

# Write data to SQLite database
df.to_sql('cars', 'sqlite:///cars.sqlite', if_exists='replace', index=False)
