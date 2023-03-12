
"""
Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
Você deverá aplicar as seguintes funções no exercício:
map
filter
sorted
sum
Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
a lista dos 5 maiores números pares em ordem decrescente;
a soma destes valores.
"""

with open('number.txt') as arquivo:
    numbers = arquivo.readlines()
numbers = [x.rstrip('\n') for x in numbers] 

numbers2 = list(map(int, numbers))

numbers3 = sorted(filter(lambda x: x % 2 == 0, numbers2), reverse=True)

numbers4 = (numbers3[0:5])
print(numbers4)

print(sum(numbers4))