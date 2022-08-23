"""
- Load the taxi data.
- Remove all rows with either total_amount <= 0 or
  passenger_count == 0
- Create a bar chart of average tip % per passenger_count
- Create a bar chart of average tip % per day of week
"""

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
len(df)

# %% Drop bad data
bad = df[
    (df['total_amount'] <= 0) |
    (df['passenger_count'] == 0)
]
df.drop(bad.index, inplace=True)
len(df)

# %% Helper column
df['tip_pct'] = \
    df['tip_amount'] / df['total_amount'] * 100

# %% Passenger Count

by_count = (
    df.groupby('passenger_count')
    ['tip_pct']
    .mean()
)
ax = by_count.plot.bar(
    title='Tip % by Passenger Count',
    rot=0,
)
ax.set_ylabel('Tip %')

# %% Week Day
from calendar import day_abbr

day_of_week = \
    df['tpep_pickup_datetime'].dt.weekday
by_day = (
    df.groupby(day_of_week)
    ['tip_pct']
    .mean()
)
by_day.index.name = 'Day of Week'
ax = by_day.plot.bar(title='Tip % by Day', rot=45)
ax.set_ylabel('Tip %')
ax.set_xticklabels(
    [day_abbr[v] for v in ax.get_xticks()])
None  # quell ax output
# %%
