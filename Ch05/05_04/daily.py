# %%
import pandas as pd

time_cols = [
    'tpep_pickup_datetime',
    'tpep_dropoff_datetime',
]
df = pd.read_csv(
    'taxi.csv',
    parse_dates=time_cols,
)
vendors = {
    1: 'Creative',
    2: 'VeriFone',
}
df['Vendor'] = \
    df['VendorID'].map(vendors).astype('category')

# %%
df['tpep_pickup_datetime'].head()

# %%
ts = pd.Timestamp(2021, 11, 1, 14, 37, 39, 3920)
ts

# %%
ts.floor('D')

# %%
df['tpep_pickup_datetime'].head().floor('D')

# %%
df['tpep_pickup_datetime'].head().dt.floor('D')

# %%
keys = \
    df['tpep_pickup_datetime'].dt.floor('D')
df.groupby(keys)

# %%
df.groupby(keys).count()

# %%
(
    df.groupby(keys)
    .count()
    ['VendorID']
    .plot.bar()
)

# %%
s = (
    df.groupby(keys)
    .count()
    ['VendorID']
)
s.index = s.index.day
s.index.name = 'Date'
ax = s.plot.bar(
    title='Daily Taxi Rides (Jan 2016)',
    rot=0,
)
ax.set_ylabel('Number of Rides')
