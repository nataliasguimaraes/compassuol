#O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

from csv import DictReader

with open('./actors.csv') as file:
    csv_reader = DictReader(file)
    data = list(csv_reader)
    

    frequenciaFilmes = []
    noRepetaMovie = []
  
    indiceMaiorNumFilme=0
    countAtual=0
    countAnterior=0
    
    
    for indice, elementos in enumerate(data):
      
      if(not (elementos['#1 Movie'] in noRepetaMovie)):
        noRepetaMovie.append(elementos['#1 Movie'])
        for elementosIterable in data:
          if(elementos['#1 Movie'] == elementosIterable['#1 Movie']):
            countAtual = countAtual +1

        if(countAtual > countAnterior):
          countAnterior = countAtual
          indiceMaiorNumFilme = indice
        
        frequenciaFilmes.append(countAtual)
        
        countAtual = 0
        
  
    print(f'Nome do filme: {noRepetaMovie[indiceMaiorNumFilme]}. Frequência: {frequenciaFilmes[indiceMaiorNumFilme]}')