# %%
import pandas as pd

csv_file = 'taxi.csv'
df = pd.read_csv(csv_file)
print(f'{len(df):,}')

# %%
df.iloc[0]

# %%
df.dtypes

# %%
time_cols = [
    'tpep_pickup_datetime',
    'tpep_dropoff_datetime',
]
df = pd.read_csv(
    csv_file,
    parse_dates=time_cols,
)
df.dtypes