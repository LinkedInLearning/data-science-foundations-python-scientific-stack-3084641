from urllib.request import urlretrieve

dl_size = 0

def reporthook(_, size, total):
    global dl_size

    dl_size += size
    precent = dl_size / total * 100
    print(f' {precent:.2f}%', end='\r')

data_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-08.parquet'
out_file = 'taxi.parquet'
urlretrieve(data_url, out_file, reporthook=reporthook)
