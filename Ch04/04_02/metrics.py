# %%
import pandas as pd

df = pd.read_csv(
    'metrics.csv',
    parse_dates=['time'],
    index_col='time',
)

(
    df.query('metric == "cpu"')
    .rolling('1min', center=True)
    .mean()
    .plot(title='CPU')
)