#3 O ator/atriz com a maior média por filme. (media por ator)

from csv import DictReader

with open('./actors.csv') as file:
    csv_reader = DictReader(file)
    data = list(csv_reader)
    

    maiorAveragePerMovie = 0
    nomeAtor= ''
    for elementos in data:
     averagePerMovie =  float(elementos['Average per Movie'])
     if(maiorAveragePerMovie<averagePerMovie):
       nomeAtor= elementos['Actor']
       maiorAveragePerMovie=averagePerMovie
    print(f'O ator/atriz com maior média por filmes é {nomeAtor} com {maiorAveragePerMovie} filmes.')