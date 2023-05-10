import pandas as pd
import json
import requests

df = pd.read_csv('movies.csv', encoding='utf-8', sep='|', low_memory=False)

df_filtered = df[df['genero'].isin(['Romance'])]

filtered_ids = df_filtered['id'].tolist()[:400]


api_key = 'eafc064d0d3e2ece1e26a68dea78eafb'
url_base = f'https://api.themoviedb.org/3/movie/{{movie_id}}?api_key={api_key}&language=pt-BR'

batch_size = 100
num_batches = (len(filtered_ids) + batch_size - 1) // batch_size

for i in range(num_batches):
    batch_ids = filtered_ids[i*batch_size : (i+1)*batch_size]
    movies = []
    for movie_id in batch_ids:
        url = url_base.format(movie_id=movie_id)
        response = requests.get(url)
        if response.status_code == 200:
            movie_data = json.loads(response.content)
            movies.append(movie_data)
    data = {"movies": movies}
    filename = f"movies_filtered_{i+1}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)