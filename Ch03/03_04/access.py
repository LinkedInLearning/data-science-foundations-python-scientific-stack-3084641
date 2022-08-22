# %%
import pandas as pd

csv_file = 'track.csv'
df = pd.read_csv(csv_file, parse_dates=['time'])

# %%
df['lat']

# %%
df.lat # Don't do this!

# %%
df[['lat', 'lng']]

# %%
df['lat'][0]

# %%
df.loc[0]

# %%
df.loc[2:7]

# %%
df[['lat', 'lng']][2:7]

# %%

df.index
# %%
import numpy as np

df1 = pd.DataFrame(
    np.arange(10).reshape(5, 2),
    columns=['x', 'y'],
    index=['a', 'b', 'c', 'd', 'e'],
)
df1

# %%
df1.loc[0]

# %%
df1.loc['a']

# %%
df1.loc['a':'d']

# %%
df1.iloc[0]

# %%
df.index

# %%
df.index = df['time']
df.index

# %%
df.loc[0]

# %%
df.loc['2015-08-20 03:48:34']

# %%

df.loc['2015-08-20 03:48']