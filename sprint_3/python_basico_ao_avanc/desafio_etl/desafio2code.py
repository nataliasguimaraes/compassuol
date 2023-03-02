#2. A média do número de filmes por autor.

from csv import DictReader

with open('./actors.csv') as file:
    csv_reader = DictReader(file)
    data = list(csv_reader)
    

    totalMovie = 0
    for elementos in data:
     totalMovie = totalMovie + int(elementos['Number of Movies'])
     mediaNumFilmes = totalMovie/len(data)
    print(f'A média do número de filmes por autor é: {mediaNumFilmes}.')