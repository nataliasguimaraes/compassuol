#2. Apresente a média da coluna contendo o número de filmes.


import pandas

df = pandas.read_csv('actors.csv')

media_coluna_filmes = df['Number of Movies'].mean()

print(f'A média da coluna contendo o número de filmes é {media_coluna_filmes}.')