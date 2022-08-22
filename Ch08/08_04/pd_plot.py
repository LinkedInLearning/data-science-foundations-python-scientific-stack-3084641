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
msft['Close'].plot()

# %%
msft['Close'].plot.kde()

# %%
(
    df
    .pivot(
        columns='Symbol',
        values='Volume'
    )
    .resample('M')
    .sum()
    .plot.bar(xticks=range(12), rot=0)
)