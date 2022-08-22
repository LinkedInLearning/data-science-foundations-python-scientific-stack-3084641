from urllib.request import urlopen

data_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-08.parquet'
with urlopen(data_url) as fp, open('taxi.csv', 'wb') as out:
    for lnum, line in enumerate(fp, 1):
        out.write(line)
        if lnum == 10_001:
            break