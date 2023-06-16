"""
QUESTÃ0 21

Implemente duas classes Pato e Pardal que herdem de uma classe Passaro a habilidade de voar
e emitir som, porém, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita)
no console.

Imprima no console exatamente assim:

Pato
Voando...
Pato emitindo som...
Quack Quack
Pardal
Voando...
Pardal emitindo som...
Piu Piu
"""
class Passaro:

  def __init__(self, som, voar):
    self.som = som
    self.voar = 'Voando...'


class Pato(Passaro):
  som = 'Quack Quack'

  def __init__(self, voar):
    super().__init__(Pato.som, voar)

  def animal(self):
    print(f'Pato \n{self.voar} \nPato emitindo som... \n{Pato.som}')


class Pardal(Passaro):
  som = 'Piu Piu'

  def __init__(self, voar):
    super().__init__(Pardal.som, voar)

  def animal(self):
    print(f'Pardal \n{self.voar} \nPardal emitindo som...\n{Pardal.som} ')


passaro1 = Pato('Voando...')

passaro1.animal()

passaro2 = Pardal('Voando...')

passaro2.animal()