"""
QUESTÃ0 10

Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados.
Utilize a lista a seguir para testar sua função.
['abc', 'abc', 'abc', '123', 'abc', '123', '123']
"""

test = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def remove_duplicates(datas):
  test2 = list(set(datas))
  return test2

print(remove_duplicates(test))