from urllib.request import urlretrieve
from pathlib import Path

here = Path(__file__).absolute().parent
csv_file = here / 'weather.csv'

url = (
    'https://www.ncei.noaa.gov/data/'
    'global-historical-climatology-network-daily/access/USW00094789.csv'
)

out_name = '/'.join(csv_file.parts[-3:])
print(f'downloading weather to {out_name}')
urlretrieve(url, csv_file)