"""
QUESTÃ0 17

Escreva uma função que recebe como parâmetro uma listae retorna 3 listas:
a lista recebida dividida em 3 partes iguais.
Teste sua implementação com a lista abaixo

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""

def partes_iguais(lista):
    parte_lista = len(lista) // 3
    parte1 = lista[:parte_lista]
    parte2 = lista[parte_lista:2*parte_lista]
    parte3 = lista[parte_lista*2:]
    return parte1, parte2, parte3
 

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
parte1, parte2, parte3 = partes_iguais(lista)
print(f'{parte1} {parte2} {parte3}')