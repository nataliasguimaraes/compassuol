"""
QUESTÃ0 04
Escreva um código Python que imprime todos os números primos de 1 até 100.
Abaixo uma imagem de exemplo dos números primos entre 1 e 1000
Obs: Utilize a função range().
"""

for num in range(1, 101): 
  if num > 1: 
    for c in range(2, num): 
        if(num % c == 0): 
            break
    else: 
        print(num)