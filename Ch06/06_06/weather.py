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
wdf = pd.read_csv(
    'weather.csv',
    parse_dates=['DATE'],
    index_col='DATE'
)
wdf.head()

# %%
wdf.describe()

# %%
from scipy.constants import convert_temperature

wdf['tempF'] = convert_temperature(
    wdf['TMAX']/10, 'C', 'F')
wdf['tempF'].sample(10)

# %%
ddf = (
    df.groupby(
        df['tpep_pickup_datetime'].dt.date)
    .count()
)
ddf.head()

# %%
jdf = pd.merge(
    ddf, wdf,
    left_index=True, right_index=True,
)
jdf.head()

# %%
jdf.plot.scatter(x='tempF', y='Vendor');