"""
QUESTÃ0 16

Escreva uma função que recebe uma string de números separados por vírgula
e retorne a soma de todos eles. Depois imprima a soma dos valores.

A string deve ter valor  "1,3,4,6,10,76"
"""

values = "1,3,4,6,10,76"


def sum_values(values):
  newvalues = list(map(int, values.split(',')))
  
  return sum(newvalues)

result = sum_values(values)

print(result)