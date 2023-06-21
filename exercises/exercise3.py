import pandas as pd
import sqlite3
from io import BytesIO
import requests

# Download the CSV file
url = "https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv"
response = requests.get(url)
data = response.content

# Read CSV data into a DataFrame
df = pd.read_csv(BytesIO(data), encoding='iso-8859-1', skiprows=6, skipfooter=4)

# Rename columns
columns_mapping = {
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
df = df.rename(columns=columns_mapping)

# Keep only required columns
required_columns = list(columns_mapping.values())
df = df[required_columns]

# Validate and filter data
df = df[df['CIN'].str.match(r'^0?\d{5}$')]
df = df[df[required_columns[3:]].apply(lambda x: x.str.isnumeric() & (x.astype(int) > 0)).all(axis=1)]

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
conn = sqlite3.connect('cars.sqlite')
cursor = conn.cursor()

# Create "cars" table
create_table_query = '''
CREATE TABLE IF NOT EXISTS cars (
    date TEXT,
    CIN TEXT,
    name TEXT,
    petrol INTEGER,
    diesel INTEGER,
    gas INTEGER,
    electro INTEGER,
    hybrid INTEGER,
    plugInHybrid INTEGER,
    others INTEGER
);
'''
cursor.execute(create_table_query)

# Insert data into "cars" table
df.to_sql('cars', conn, if_exists='replace', index=False)

# Commit changes and close the database connection
conn.commit()
conn.close()
