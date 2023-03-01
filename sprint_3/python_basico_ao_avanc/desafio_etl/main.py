"""
Armazene o arquivo actors.csv dentro de uma nova pasta,
após isso crie 5 arquivos do tipo “txt” vazios (1 para cada exercício do desafio).

Em seguida para cada uma das tarefas da sequencia,
leia o arquivo actors.csv utilizando Python como linguagem de programação
e depois de obter as repostas necessárias armazene cada um dos resultados em um dos arquivos “txt” criados.

Perguntas dessa tarefa
1. O ator/atriz com maior número de filmes e o respectivo número de filmes.

2. A média do número de filmes por autor.

3. O ator/atriz com a maior média por filme.

4. O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

5. A lista dos Autores ordenada por pagamento. Do mais bem pago para o menos bem pago
"""


from csv import reader

with open ('actors.csv') as arquivo:
  leitura = reader(arquivo)
  for linha in leitura:
  #cada linha é uma lista
    print(linha)

  linha = []

  valores = linha.strip().split(',')

  for i in range(len(valores)):
    valores[i] = valores[i].replace(',', ' ')

linha_modificada = ','.join(valores)
linha.append(linha_modificada)