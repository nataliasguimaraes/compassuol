"""
A função calcular_valor_maximo deve receber dois parâmetros, chamados de operadores e operandos. Em operadores, espera-se uma lista de caracteres que representam as operações matemáticas suportadas (+, -, /, *, %), as quais devem ser aplicadas à lista de operadores nas respectivas posições. Após aplicar cada operação ao respectivo par de operandos, a função deverá retornar o maior valor dentre eles.
Veja o exemplo:
Entrada
operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]
Aplicar as operações aos pares de operandos
[ 3+6 , -7-4.9, 8*-8 , 10/2 , 8+4 ] 
Obter o maior dos valores
12
Na resolução da atividade você deverá aplicar as seguintes funções:
max
zip
map
"""
def calcular_valor_maximo(operadores, operandos):
  operacoes = {
  "+": lambda op1, op2: op1 + op2,
  "-": lambda op1, op2: op1 - op2,
  "*": lambda op1, op2: op1 * op2,
  "/": lambda op1, op2: op1 / op2,
  '%': lambda x, y: x % y,
  }
  op_results = list(map(lambda x: operacoes[x[1]](*x[0]), zip(operandos, operadores)))
  return max(op_results)

operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]
print(calcular_valor_maximo(operadores, operandos))