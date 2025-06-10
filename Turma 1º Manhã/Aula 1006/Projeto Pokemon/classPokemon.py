class Pokemon:
    def __init__(self, especie, nroPokedex, tipo, hp, atk, defesa):
        self.especie = especie
        self.nroPokedex = nroPokedex
        self.tipo = tipo
        self.hp = hp
        self.atk = atk
        self.defesa = defesa
    def mostrarInformacoes(self):
        print(f'''
------ Poke Entry ------

Número Pokedex: {self.nroPokedex}
Espécie: {self.especie}
Tipo: {self.tipo}
HP: {self.hp}
Ataque: {self.atk}
Defesa: {self.defesa}
''')
    def atacar(self, inimigo):
        dano = int(10 * (self.atk/inimigo.defesa))

        print(f"{self.especie} atacou {inimigo.especie} causando {dano} de dano!")
        inimigo.hp -= dano
        print(f"{inimigo.especie} possui {inimigo.hp} de hp restante!")

class PokemonFogo(Pokemon):
    def __init__(self, especie, nroPokedex, hp, atk, defesa):
        super().__init__(especie, nroPokedex, "Fogo", hp, atk, defesa)
        
class PokemonAgua(Pokemon):
    def __init__(self, especie, nroPokedex, hp, atk, defesa):
        super().__init__(especie, nroPokedex, "Água", hp, atk, defesa)

class PokemonGrama(Pokemon):
    def __init__(self, especie, nroPokedex, hp, atk, defesa):
        super().__init__(especie, nroPokedex, "Grama", hp, atk, defesa)