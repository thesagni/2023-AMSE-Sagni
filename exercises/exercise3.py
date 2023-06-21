import pandas as pd
from sqlalchemy import String, TEXT, INTEGER, Float, DECIMAL,BIGINT

cols_sql = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]
# Download the CSV file
url = "https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv"
df = pd.read_csv(url, encoding="latin1", skiprows=6, skipfooter=4, usecols=cols_sql)

# Rename columns
cols_map = {
    'A': 'date',
    'B': 'CIN',
    'C': 'name',
    'M': 'petrol',
    'W': 'diesel',
    'AG': 'gas',
    'AQ': 'electro',
    'BA': 'hybrid',
    'BK': 'plugInHybrid',
    'BU': 'others'
}
df = df.rename(columns=cols_map)

# Keep only required columns
required_cols = list(cols_map.values())
df = df[required_cols]

# Validate and filter data
df = df[df['CIN'].str.match(r'^0?\d{5}$')]
df = df[df[required_cols[3:]].apply(lambda x: x.str.isnumeric() & (x.astype(int) > 0)).all(axis=1)]

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

# Create SQLite database and write data to the "cars" table
df.to_sql('cars','sqlite:///cars.sqlite', if_exists='replace', index=False)
