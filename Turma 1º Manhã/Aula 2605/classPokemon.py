import random
class Pokemon:
    def __init__(self, especie, tipo, hp, atk, defesa):
        self.especie = especie
        self.tipo = tipo
        self.hp =int( hp * (random.randint(80,120)/100) )
        self.atk = int( atk * (random.randint(80,120)/100) )
        self.defesa = int( defesa * (random.randint(80,120)/100) )
    def mostrarInformacoes(self):
        print(f'''
----- PokeEntry {self.especie} -----

Espécie: {self.especie}
Tipo: {self.tipo}
HP: {self.hp}
Atk: {self.atk}
Defesa: {self.defesa}
''')
    