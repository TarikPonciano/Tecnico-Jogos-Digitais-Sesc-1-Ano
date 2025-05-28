class Pokemon:
    def __init__(self, especie, hp, atk, defesa, level, tipo):
        self.especie = especie
        self.hp = hp
        self.atk = atk
        self.defesa = defesa
        self.level = level
        self.tipo = tipo
    def mostrarInformacoes(self):
        print(f'''
----- Informações -----
    Espécie: {self.especie}
    Level: {self.level}
    HP: {self.hp}
    ATK: {self.atk}
    Defesa: {self.defesa}
    Tipo: {self.tipo}
''')
        
class PokemonFogo(Pokemon):
    def __init__(self, especie, hp, atk, defesa, level):
        super().__init__(especie, hp, atk, defesa, level, "Fogo")
        