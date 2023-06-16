"""
2. [Warm up] Em Python, declare e inicialize uma lista contendo o nome de 20 animais.
Ordene-os em ordem crescente e itere sobre os itens, imprimindo um a um (você pode utilizar list comprehension aqui). 
Na sequência, armazene o conteúdo da lista em um arquivo de texto, um item em cada linha, no formato CSV.
"""
animais = ['cachorro', 'gato', 'periquito', 'papagaio', 'vaca', 'leao', 'tigre', 'hipopotamo', 'zebra', 'arara', 'macaco', 'girafa', 'boi', 'baleia', 'rinoceronte', 'borboleta', 'minhoca', 'pombo', 'grilo', 'coelho']

animais.sort()

[print(a) for a in animais]

with open('animais.csv', 'w', newline="") as f:
    for animal in animais:
        f.write(animal + ',\n')