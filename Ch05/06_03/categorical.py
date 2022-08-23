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
df.dtypes

# %%
df['VendorID'].unique()

# %%
vendors = {
    1: 'Creative',
    2: 'VeriFone',
}
df['Vendor'] = df['VendorID'].map(vendors)
df['Vendor'].head()

# %%
mb = 2**20
df['Vendor'].memory_usage(deep=True) / mb

# %%
df['Vendor'] = (
    df['VendorID']
    .map(vendors)
    .astype('category')
)
df['Vendor'].head()

# %%
df['Vendor'].memory_usage(deep=True) / mb

# %%
df['Vendor'].head().cat.codes

# %%
len(df[df['Vendor'] == 'VeriFone'])