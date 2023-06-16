"""
QUESTÃ0 16

Escreva uma função que recebe uma string de números separados por vírgula
e retorne a soma de todos eles. Depois imprima a soma dos valores.

A string deve ter valor  "1,3,4,6,10,76"
"""

class Lampada:
  def __init__(self,ligada):
    self.ligada = ligada
  def liga(self):
    self.ligada = True
  def desliga (self):
    self.ligada = False
  def esta_ligada(self):
    return self.ligada

lampada = Lampada(False)

lampada.liga()
print(lampada.esta_ligada())
lampada.desliga()
print(lampada.esta_ligada())