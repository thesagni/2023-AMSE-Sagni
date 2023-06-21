import pandas as pd 

from io import StringIO

url = 'https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv'
cols = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]
column_names = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']
skiprows = 6

response = requests.get(url)
data = response.text.split('\n')[skiprows:-4]
data = '\n'.join(data)

df = pd.read_csv(StringIO(data), sep=';', encoding='iso-8859-1', header=None, usecols=cols, names=column_names,
                 engine='python', na_values='.', thousands=',', dtype={'CIN': str})

# Filter out rows with '-' in petrol column
df = df[df['petrol'].apply(lambda x: '-' not in str(x))]


# Ensure 'CIN' column has exactly five characters
df = df[df['CIN'].str.len() == 5]

# Convert data types
dtypes = {'petrol': 'int64', 'diesel': 'int64', 'gas': 'int64', 'electro': 'int64',
              'hybrid': 'int64', 'plugInHybrid': 'int64', 'others': 'int64'}
df = df.astype(dtypes)

# Write data to SQLite database
df.to_sql('cars', 'sqlite:///cars.sqlite', if_exists='replace', index=False)
