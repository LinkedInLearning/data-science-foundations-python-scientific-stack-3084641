# %%
from shapely.geometry import Point

pt = Point(1, 2)
pt

# %%
pt.x, pt.y

# %%
from shapely.geometry import Polygon

poly = Polygon([
    [0, 0],
    [0, 10],
    [10, 10],
    [10, 0],
])
poly

# %%
poly.area

# %%
poly.centroid

# %%
poly.intersects(pt)

# %%
poly.intersects(Point(10, 20))

# %%
import pandas as pd

df = pd.read_csv(
    'track.csv',
    parse_dates=['time'],
    index_col='time',
)
df = df.resample('min').mean()

# %%
df['point'] = (
    df[['lat', 'lng']]
    .apply(Point, axis=1)
)
df.head()

# %%
mid_lat, max_lat = \
    df['lat'].mean(), df['lat'].max()
mid_lng, max_lng = \
    df['lng'].mean(), df['lng'].max()
poly = Polygon([
    [mid_lat, mid_lng],
    [mid_lat, max_lng],
    [max_lat, max_lng],
    [max_lat, mid_lng],
])
poly

# %%
df[df['point'].apply(poly.intersects)]

# %%
poly.exterior.xy
# %%
import numpy as np

np.stack(poly.exterior.xy)

# %%
np.stack(poly.exterior.xy).T

# %%
import folium

m = folium.Map(
    location=[df['lat'].mean(), df['lng'].mean()],
    zoom_start=15,
)
points = np.stack(poly.exterior.xy).T
m.add_child(folium.PolyLine(points))
m

# %%
center = [df['lat'].mean(), df['lng'].mean()]
m = folium.Map(
    location=center,
    zoom_start=15,
)
m.add_child(folium.PolyLine(points))

def add_marker(row):
    loc = tuple(row[['lat', 'lng']])
    in_poly = poly.intersects(row['point'])
    marker = folium.CircleMarker(
        loc,
        radius=5,
        color='yellow' if in_poly else 'green',
        popup=row.name.strftime('%H:%M'),
    )
    marker.add_to(m)

df.apply(add_marker, axis=1)
m