import pandas as pd
import json
import requests

df = pd.read_csv('movies.csv', encoding='utf-8', sep='|', low_memory=False)

df['anoLancamento'] = pd.to_datetime(df['anoLancamento'], format='%Y', errors='coerce')
df = df.dropna(subset=['anoLancamento'])

df_filtered = df.loc[(df['anoLancamento'].dt.year >= 2000) & (df['genero'].isin(['Romance', 'Drama']))]

filtered_ids = list(set(df_filtered['id'].tolist()))


api_key = '***'
url_base = 'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=pt-BR"'

movies = []
for movie_id in filtered_ids:
    url = url_base.format(movie_id=movie_id, api_key=api_key)
    response = requests.get(url)
    if response.status_code == 200:
        movie_data = json.loads(response.content)
        if 'id' in movie_data and movie_data['id'] == movie_id:
            movies.append(movie_data)

data = {"movies": movies}

with open('tmdb_movies_filtered.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)