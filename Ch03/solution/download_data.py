from urllib.request import urlretrieve

url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-08.parquet'
out_file = 'taxi.parquet'
urlretrieve(url, out_file)
