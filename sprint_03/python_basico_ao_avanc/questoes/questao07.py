"""
QUESTÃ0 07

Dada a seguinte lista:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Faça um programa que gere uma nova lista contendo apenas números ímpares.
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
impar = []

for item in a:
  if item % 2 != 0:
    impar.append(item)
print(impar)
