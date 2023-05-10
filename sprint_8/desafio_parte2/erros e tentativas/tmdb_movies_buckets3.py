import pandas as pd
import json
import requests
import boto3
from datetime import datetime

df = pd.read_csv('movies.csv', encoding='utf-8', sep='|', low_memory=False)

df_filtered = df[df['genero'].isin(['Romance'])]

filtered_ids = df_filtered['id'].tolist()[:100]


api_key = 'eafc064d0d3e2ece1e26a68dea78eafb'
url_base = 'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=pt-BR"'

movies = []
for movie_id in filtered_ids:
    url = url_base.format(movie_id=movie_id, api_key=api_key)
    response = requests.get(url)
    if response.status_code == 200:
        movie_data = json.loads(response.content)
        movies.append(movie_data)

data = {"movies": movies}

json_data = json.dumps(data, ensure_ascii=False, indent=4)

file_name = 'tmdb_filtered_movies.json'

session = boto3.Session(profile_name="573862076861_AdministratorAccess", region_name="us-east-1")
s3 = boto3.resource('s3')
bucket_name = 'natalias-s3-bucket'
bucket_movies_directory = f'Raw/Local/JSON/Movies/{datetime.now().strftime("%Y/%m/%d")}/{file_name}'
s3.Object(bucket_name, bucket_movies_directory).put(Body=json_data)
