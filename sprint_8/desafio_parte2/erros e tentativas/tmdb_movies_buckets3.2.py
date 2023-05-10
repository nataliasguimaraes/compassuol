import pandas as pd
import json
import requests
import boto3
from datetime import datetime

# LEITURA CSV BUCKET AWS

bucket_name = 'natalias-s3-bucket'
s3_file_name = 'Raw/Local/CSV/Movies/2023/04/26/movies.csv'
s3_client = boto3.client('s3')
s3 = boto3.resource('s3')
response = s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)
df_movies = pd.read_csv(response['Body'], sep='|', na_values=['\\N', 'NA'])

df_filtered = df_movies[df_movies['genero'].isin(['Romance'])]

filtered_ids = df_filtered['id'].tolist()[:100]

# CONSUMIR DADOS API TMDB
api_key = 'eafc064d0d3e2ece1e26a68dea78eafb'
url_base = 'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=pt-BR"'

movies = []
for movie_id in filtered_ids:
    url = url_base.format(movie_id=movie_id, api_key=api_key)
    response = requests.get(url)
    if response.status_code == 200:
        movie_data = json.loads(response.content)
        movies.append(movie_data)

# GRAVAR DADOS JSON NO BUCKET DA AQWS

data = {"movies": movies}

json_data = json.dumps(data, ensure_ascii=False, indent=4)

file_name = 'tmdb_filtered_movies.json'

session = boto3.Session(profile_name="573862076861_AdministratorAccess", region_name="us-east-1")
s3 = boto3.resource('s3')
bucket_name = 'natalias-s3-bucket'
bucket_movies_directory = f'Raw/Local/JSON/Movies/{datetime.now().strftime("%Y/%m/%d")}/{file_name}'
s3.Object(bucket_name, bucket_movies_directory).put(Body=json_data)
