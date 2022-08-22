# %%
import pandas as pd

csv_file = 'track.csv'
df = pd.read_csv(csv_file, parse_dates=['time'])
df

# %%
import numpy as np

lat_km = 92
lng_km = 111


def distance(lat1, lng1, lat2, lng2):
    delta_lat = (lat1 - lat2) * lat_km
    delta_lng = (lng1 - lng2) * lng_km
    return np.hypot(delta_lat, delta_lng)
# %%
lat1, lng1 = df.loc[200]['lat'], df.iloc[200]['lng']
lat2, lng2 = df.loc[201]['lat'], df.iloc[201]['lng']
distance(lat1, lng1, lat2, lng2)
# %%
s = pd.Series(np.arange(5))
s

# %%
s.shift()

# %%
s.shift(-1)


# %%
dist = distance(
    df['lat'], df['lng'], 
    df['lat'].shift(), df['lng'].shift(),
)
dist[:5]

# %%
dist.sum()

# %%
times = df['time'].diff()
times[:5]

# %%
times.sum()

# %%

times_hour = times / pd.Timedelta(1, 'hour')
times_hour[:5]

# %%
speed = dist / times_hour
speed[:5]