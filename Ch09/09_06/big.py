# %%
import sqlite3

import pandas as pd
from tqdm import tqdm

time_cols = [
    'tpep_pickup_datetime',
    'tpep_dropoff_datetime',
]

with sqlite3.connect('taxi.db') as conn:
    chunks = pd.read_csv(
        'taxi.csv',
        parse_dates=time_cols,
        chunksize=100_000)

    for chunk in tqdm(chunks):
        chunk.to_sql(
            'rides',
            conn,
            index=False,
            if_exists='append',
        )

# %%
sql = '''
SELECT
    passenger_count,
    COUNT(VendorID) AS count
FROM rides
WHERE passenger_count > 1
GROUP BY passenger_count
'''

df = pd.read_sql(sql, conn)
df

# %%
import dask.dataframe as dd

ddf = dd.read_csv(
    'taxi.csv',
    parse_dates=time_cols,
    dtype={'VendorID': 'float64'},
)

# %%
ddf['VendorID'].value_counts()

# %%
ddf['VendorID'].value_counts().compute()
