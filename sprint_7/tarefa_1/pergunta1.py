#1. Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.


import pandas

df = pandas.read_csv('actors.csv')

maior_num_filmes = df.loc[df['Number of Movies'].idxmax(), 'Actor']
num_filmes = df['Number of Movies'].max()

print(f'O ator/atriz com maior número de filmes é {maior_num_filmes} com {num_filmes} filmes.')