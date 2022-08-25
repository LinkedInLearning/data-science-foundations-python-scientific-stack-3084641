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
df['hour'] = \
    df['tpep_pickup_datetime'].dt.hour
df['day'] = \
    df['tpep_pickup_datetime'].dt.date
df[['day', 'hour']].head()

# %%
(
    df.groupby(['Vendor', 'day', 'hour'])
    .count()
    ['Vendor']
)

# %%
(
    df.groupby(['Vendor', 'day', 'hour'])
    .count()
    .index
)

# %%
(
    df.groupby(
        ['Vendor', 'day', 'hour'],
        as_index=False
    )
    .count()
    .columns
)

# %%
daily_df = (
    df
    .groupby(['Vendor', 'day', 'hour'], as_index=False)
    .count()
)
hourly_df = (
    daily_df
    .groupby(['Vendor', 'hour'], as_index=False)
    ['VendorID']
    .median()
)
hourly_df

# %%
hourly_df.pivot(
    columns='Vendor',
    index='hour',
    values='VendorID'
).plot.bar(rot=0)