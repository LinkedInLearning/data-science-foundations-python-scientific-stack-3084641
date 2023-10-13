# What is the mean speed (mile/hour) in taxi.parquet?

# - Run download_data.py to download the data
# %%
# Import libraries and create a data frame using the file
import pandas as pd
from pathlib import Path

file = Path('taxi.parquet')
df = pd.read_parquet(file)
df.head()
# %%
# Check the data types of the time columns
df.dtypes
# %%
mask = df['tpep_dropoff_datetime'] > df['tpep_pickup_datetime']
df = df[mask]
# %%
times = df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']
times_hour = times / pd.Timedelta(1, 'hour')
speed = df['trip_distance'] / times_hour
# %%
speed.mean()
# %%
