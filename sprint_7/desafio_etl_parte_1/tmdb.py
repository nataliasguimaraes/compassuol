import boto3
import json
import requests
from datetime import datetime

api_key = 'eafc064d0d3e2ece1e26a68dea78eafb'
base_url = 'https://api.themoviedb.org/3/movie/76341?api_key=<<eafc064d0d3e2ece1e26a68dea78eafb>>'


#Conexão S3
#bucket_name = 'seu_bucket'
#storage_layer = 'Raw'
#data_source = 'TMDB'
#data_format = 'JSON'
#data_specification = 'movie_details'
#s3 = boto3.resource('s3')

# def max100 registros
#def split_data(data):
#    for i in range(0, len(data), 100):
#        yield data[i:i + 100]

#GET API TMDB para JSON
response = requests.get(base_url + 'now_playing', params={'api_key': api_key})
movies_data = json.loads(response.text)

# max 100 registros cada
movies_data_list = list(split_data(movies_data['results']))

# Define o nome do arquivo com base na data de processamento
now = datetime.now()
file_name = '{}-{}-{}_{}.json'.format(now.year, now.month, now.day, now.strftime("%H%M%S"))

# Salva cada arquivo com os dados no S3, seguindo o padrão de path especificado
for i, data in enumerate(movies_data_list):
    object_name = '{}/{}/{}/{}/{}/{}/{}/{}'.format(storage_layer, data_source, data_format, data_specification, now.year, now.month, now.day, '{}_{}'.format(i, file_name))
    s3.Object(bucket_name, object_name).put(Body=json.dumps(data))
