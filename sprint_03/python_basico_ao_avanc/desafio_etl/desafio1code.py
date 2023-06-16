#1. O ator/atriz com maior número de filmes e o respectivo número de filmes.


from csv import DictReader

with open('./actors.csv') as file:
    csv_reader = DictReader(file)
    data = list(csv_reader)


    maiorNumberMovies = 0
    nomeAtor = ''
    for elementos in data:
     numberMovies =  int(elementos['Number of Movies'])
     if(maiorNumberMovies<numberMovies):
       nomeAtor = elementos['Actor']
       maiorNumberMovies = numberMovies
    print(f'O ator com maior número de filmes é {nomeAtor} com {maiorNumberMovies} filmes.')