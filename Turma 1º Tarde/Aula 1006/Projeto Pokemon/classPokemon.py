class Pokemon:
    def __init__(self, nroPokedex, especie, tipo, hp, atk, defesa):
        self.nroPokedex = nroPokedex
        self.especie = especie
        self.tipo = tipo
        self.hp = hp
        self.atk = atk
        self.defesa = defesa
        
    def mostrarInformacoes(self):
        print(f'''
------- Poke Entry -------
              
Número: {self.nroPokedex}
Espécie: {self.especie}
Tipo: {self.tipo}
HP: {self.hp}
ATK: {self.atk}
DEF: {self.defesa}

''')
    def atacar(self, inimigo):
        
        dano = int(10 * (self.atk/inimigo.defesa))
        inimigo.hp -= dano

        print(f"{self.especie} atacou {inimigo.especie} e causou {dano} de dano!")
        print()
        print(f"{inimigo.especie} possui {inimigo.hp} de vida restante!")

