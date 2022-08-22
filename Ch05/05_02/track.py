# %%
import pandas as pd

df = pd.read_csv(
    'track.csv',
    parse_dates=['time'],
    index_col='time',
)

# %%
import folium

center = [df['lat'].mean(), df['lng'].mean()]
m = folium.Map(
    location=center,
    zoom_start=15,
)

loc = tuple(df.iloc[100][['lat', 'lng']])
marker = folium.Marker(loc)
marker.add_to(m)
m

# %%
m = folium.Map(
    location=center,
    zoom_start=15,
)
marker = folium.CircleMarker(
    loc,
    color='red')
marker.add_to(m)
m

# %%
m = folium.Map(
    location=center,
    zoom_start=15,
)
marker = folium.CircleMarker(
    loc,
    color='red',
    popup='Hi there',
)
marker.add_to(m)
m

# %%
m = folium.Map(
    location=center,
    zoom_start=15,
)

def add_marker(row):
    loc = tuple(row[['lat', 'lng']])
    marker = folium.CircleMarker(
        loc,
        radius=5,
        color='red',
        popup=row.name.strftime('%H:%M'),
    )
    marker.add_to(m)

add_marker(df.iloc[200])
m
# %%
m = folium.Map(
    location=center,
    zoom_start=15,
)
df.apply(add_marker, axis=1)
m

# %%
m = folium.Map(
    location=center,
    zoom_start=15,
)
min_df = df.resample('min').mean()
min_df.apply(add_marker, axis=1)
m