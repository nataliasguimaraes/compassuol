"""
QUESTAO 01

Escreva um código Python que lê do teclado o nome e a idade de um usuário e que imprima
apenas o ano em que ele completará 100 anos.
Dica: você pode ler strings digitadas no teclado utilizando a função builtin input('mensagem').
Lembre-se de converter números para seu respectivo tipo (int ou float) antes fazer operações aritméticas.
"""

name = input("Digite seu nome: ")
age = int(input("Digite sua idade: "))

print((100-age)+2023)