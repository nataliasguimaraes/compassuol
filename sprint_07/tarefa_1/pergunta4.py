#4. Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.


import pandas

df = pandas.read_csv('actors.csv')

most_frequent_movie = df['#1 Movie'].value_counts().idxmax()
frequency = df['#1 Movie'].value_counts().max()

print(f'O nome do filme mais frequente é {most_frequent_movie} e sua respectiva frequência é de {frequency}.')