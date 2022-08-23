"""Download 10% of January 2016 taxi data to taxi.csv"""

from urllib.request import urlopen
from time import monotonic
from pathlib import Path

here = Path(__file__).absolute().parent
csv_file = here / 'taxi.csv'
url = 'https://s3.amazonaws.com/nyc-tlc/csv_backup/yellow_tripdata_2016-01.csv'
out_name = '/'.join(csv_file.parts[-3:])

start = monotonic()
with urlopen(url) as resp:
    payload_size = int(resp.headers['Content-Length'])
    size_mb = payload_size / (2**20)
    print(f'downloading 10% of {size_mb:.2f}MB to {out_name}')
    size = 0
    with open(csv_file, 'wb') as out:
        for i, line in enumerate(resp):
            size += len(line)
            prec = (size / payload_size) * 100
            print(f' {prec:.2f}%', end='\r')
            if i % 10 != 0:
                continue
            out.write(line)

if size != payload_size:
    raise SystemError(f'error: expected {payload_size} bytes, got {size}')

duration = int(monotonic() - start)
print(f'{csv_file}: {size_mb:.1f}MB downloaded in {duration} seconds')
