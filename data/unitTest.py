import pandas as pd
import sqlite3

def checkRows(table, numRows):
    con = sqlite3.connect("Bicycle_data.sqlite")
    cur = con.cursor()
    rows = cur.execute("SELECT COUNT(*) FROM " + table)
    if not rows.fetchone() == (numRows,):
        print(table + ": Not all rows have been imported into the database!")
        return False
    return True

# Downloading 1st data source
urls = [
    'https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-01.csv',
    'https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-02.csv',
    'https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-03.csv',
    'https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-04.csv',
    'https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-05.csv',
    'https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-06.csv',
    'https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-07.csv',
    'https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-08.csv',
    'https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-09.csv',
    'https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-10.csv',
    'https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-11.csv',
    'https://github.com/od-ms/radverkehr-zaehlstellen/blob/main/100031297/2021-12.csv'
]

for url in urls:
    df = pd.read_csv(url, sep=',')
    # Additional data processing steps if needed
    df.to_sql('Bicycle_Accidents', 'sqlite:///Bicycle_data.sqlite', if_exists='append', index=False)

# Downloading 2nd data source
df = pd.read_csv('C:/Users/reham/Desktop/subj sem 4/AMSE(DATA ENGG)/data/data source 2/AccidentData.csv', sep=',')

# Renaming needed rows
df.loc[24, 'rows'] = 'Total Accidents - Inside built-up areas'
df.loc[25, 'rows'] = 'Total Accidents - Outside built-up areas'
df.loc[26, 'rows'] = 'Total Accidents - On motorways/freeways'

# Saving table to SQLite file
df.to_sql('Bicycle_Accidents', 'sqlite:///Bicycle_data.sqlite', if_exists='append', index=False)

# Validate the number of rows in the table
if checkRows("Bicycle_Accidents", expected_num_rows):
    print("Data successfully imported into the database.")
