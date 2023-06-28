import os
import pandas as pd
import sqlite3

# Define the paths to the CSV file
csv_files = [
    'C:/Users/reham/Desktop/2020-06.csv',
    'C:/Users/reham/Desktop/2020-07.csv',
    'C:/Users/reham/Desktop/2020-08.csv',
    'C:/Users/reham/Desktop/2020-09.csv',
    'C:/Users/reham/Desktop/2020-10.csv',
    'C:/Users/reham/Desktop/2020-11.csv',
    'C:/Users/reham/Desktop/2020-12.csv',
    'C:/Users/reham/Desktop/2021-01.csv',
    'C:/Users/reham/Desktop/2021-02.csv',
    'C:/Users/reham/Desktop/2021-03.csv',
    'C:/Users/reham/Desktop/2021-04.csv',
    'C:/Users/reham/Desktop/2021-05.csv',
    'C:/Users/reham/Desktop/2021-06.csv',
    'C:/Users/reham/Desktop/2021-07.csv',
    'C:/Users/reham/Desktop/2021-08.csv'
]

# Read and concatenate the CSV files
dfs = []
for file in csv_files:
    df = pd.read_csv(file, encoding='latin-1')
    dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dfs)

# Rename the desired column
combined_df.rename(columns={'Unnamed: 1': 'Total Bicycle count'}, inplace=True)

# Save the combined DataFrame to a CSV file in the /data directory
combined_df.to_csv(os.path.join(data_folder, 'combined_data.csv'), index=False)

# Read the AccidentData2.excel file
accident_df =pd.read_excel('C:/Users/reham/Desktop/AccidentData2.xlsx')

# Rename the desired rows

accident_df.iloc[21, 0] = 'Total Accidents'

# Save the accident_df to a CSV file in the /data directory
accident_df.to_csv(os.path.join(data_folder, 'accident_data.csv'), index=False)

# Read the Accident Data Münster.xlsx file
munster_df = pd.read_excel('C:/Users/reham/Desktop/Accident Data Münster2.xlsx')

# Rename the desired row
munster_df.iloc[2, 0] = 'Total Accidents - Münster'

# Save the munster_df to a CSV file in the /data directory
munster_df.to_csv(os.path.join(data_folder, 'munster_data.csv'), index=False)

# Create a SQLite connection
conn = sqlite3.connect(os.path.join(data_folder, 'Bicycle_data.sqlite'))

# Save the combined_df to the SQLite database
combined_df.to_sql('Bicycle_Count', conn, if_exists='replace', index=False)

# Save the accident_df to the SQLite database
accident_df.to_sql('Accident_Data', conn, if_exists='replace', index=False)

# Save the munster_df to the SQLite database
munster_df.to_sql('Munster_Accidents', conn, if_exists='replace', index=False)

# Close the database connection
conn.close()
