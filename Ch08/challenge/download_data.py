from pathlib import Path
from urllib.request import urlopen
import pandas as pd

here = Path(__file__).absolute().parent
csv_file = here / 'stocks.csv'

dfs = []
symbols = [
    'GOOG',
    'MSFT',
    'ORCL',
]
for sym in symbols:
    print(f'downloading {sym}')
    url = f'https://query1.finance.yahoo.com/v7/finance/download/{sym}'
    url += '?period1=1577836800&period2=1609372800&interval=1d&events=history'
    with urlopen(url) as resp:
        df = pd.read_csv(resp, parse_dates=['Date'])
        df['Symbol'] = sym
        df.insert(1, 'Symbol', df.pop('Symbol'))
        dfs.append(df)
df = pd.concat(dfs)
df.sort_values('Date', inplace=True)
df.to_csv(csv_file, index=False)