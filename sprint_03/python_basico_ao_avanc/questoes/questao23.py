"""
QUESTÃ0 23

Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y,
e retorne a soma dos dois.
Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y,
e retorne a subtração dos dois (resultados negativos são permitidos).

Utilize os valores abaixo para testar seu exercício:

x = 4 
y = 5
imprima:

Somando: 4+5 = 9
Subtraindo: 4-5 = -1
"""

class Calculo():

  def soma(self, x, y):
      print(f'Somando: {x}+{y} = {x + y}')
  def subtracao(self, x, y):
      print(f'Subtraindo: {x}-{y} = {x - y}')


calculadora = Calculo()

calculadora.soma(4,5)
calculadora.subtracao(4,5)