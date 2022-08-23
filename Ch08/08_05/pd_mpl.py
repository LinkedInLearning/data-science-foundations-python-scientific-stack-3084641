# %% 
import pandas as pd

df = pd.read_csv(
    'stocks.csv',
    parse_dates=['Date'],
    index_col='Date'
)
df.head()

# %%
msft = df.query('Symbol == "MSFT"')

# %%
daily = (
    msft
    ['Volume']
    .groupby(msft.index.weekday)
    .median()
)
daily.plot.bar()

# %%
ax = daily.plot.bar(
    title='MSFT',
    rot=0,
)
ax.set_xticklabels(
    ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
)
ax.set_xlabel('Weekday')
ax.set_ylabel('Volume')