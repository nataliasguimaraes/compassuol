#3. Apresente o nome do ator/atriz com a maior média por filme.


import pandas

df = pandas.read_csv('actors.csv')

maior_media_filmes = df.loc[df['Average per Movie'].idxmax(), 'Actor']
media_total_filmes = df['Average per Movie'].max()

print(f'O nome do ator/atriz com a maior média por filme é {maior_media_filmes} com uma média de ${media_total_filmes} dólares/filme.')