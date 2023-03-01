"""
QUESTAO 02

Escreva um código Python que verifique se três números digitados pelo usuário são pares ou ímpares.
Para cada número, imprima o Par: ou Ímpar: e o número correspondente.
Exemplo de formato de saída:

Par: 2
Ímpar: 3
"""

numbers = []

for item in range(3):
  numbers.insert(item,int(input("Digite um número: "))) 

for item in numbers:
  if item % 2 == 0:
    print(f'Par: '+ str(item))
  else:
    print(f'Ímpar: '+ str(item))