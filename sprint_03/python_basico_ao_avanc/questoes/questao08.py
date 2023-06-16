"""
QUESTÃ0 08

Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']
é ou não um palíndromo.
Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.
É necessário que você imprima no console exatamente assim:

A palavra: maça não é um palíndromo
 
A palavra: arara é um palíndromo
 
A palavra: audio não é um palíndromo
 
A palavra: radio não é um palíndromo
 
A palavra: radar é um palíndromo
 
A palavra: moto não é um palíndromo
"""

lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for item in lista:
  if item[::-1] == item:
    print('A palavra: {} é um palíndromo'.format(item))
  else:
    print('A palavra: {} não é um palíndromo'.format(item))