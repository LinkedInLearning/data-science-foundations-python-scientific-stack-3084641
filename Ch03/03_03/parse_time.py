# %%
import pandas as pd

csv_file = 'track.csv'
df = pd.read_csv(csv_file)
df.dtypes
# %%
df = pd.read_csv(csv_file, parse_dates=['time'])
df.dtypes

# %%
