import pandas as pd
import json
import requests

df = pd.read_csv('movies.csv', encoding='utf-8', sep='|', low_memory=False)

df_filtered = df[df['genero'].isin(['Romance'])]

filtered_ids = df_filtered['id'].tolist()[:100]


api_key = '***'
url_base = 'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=pt-BR"'

movies = []
for movie_id in filtered_ids:
    url = url_base.format(movie_id=movie_id, api_key=api_key)
    response = requests.get(url)
    if response.status_code == 200:
        movie_data = json.loads(response.content)
        movies.append(movie_data)

data = {"movies": movies}

with open('tmdb_movies_filtered.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)