import requests
import pandas as pd
from IPython.display import display

api_key = "***"
genre_id = 10749

filmes = []
page_number = 1

while True:
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=pt-BR&sort_by=popularity.desc&with_genres={genre_id}&page={page_number}"
    response = requests.get(url)
    data = response.json()
    if not data.get("results"):
        # sai do loop se não houver mais resultados
        break
    for movie in data['results']:
        df = {
            'Titulo': movie.get('title'),
            'Data de lançamento': movie.get('release_date', ''),
            'Visão geral': movie.get('overview'),
            'Votos': movie.get('vote_count'),
            'Média de votos': movie.get('vote_average'),
            }
        filmes.append(df)
    page_number += 1

df = pd.DataFrame(filmes)
display(df)
