# %%
import pandas as pd

df = pd.read_csv(
    'track.csv',
    parse_dates=['time'],
    index_col='time',
)
df.columns

# %%
df.index[:5]

# %%
import folium

center = [df['lat'].mean(), df['lng'].mean()]
m = folium.Map(
    location=center,
    zoom_start=15,
)
m

# %%
m.save('track.html')