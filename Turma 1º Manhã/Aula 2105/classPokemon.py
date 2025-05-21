import random
class Pokemon:
    def __init__(self, especie, tipo, atk, defesa, hp):
        self.especie = especie
        self.tipo = tipo
        self.atk = atk
        self.defesa = defesa
        self.hp = hp
        if (random.randint(1,100) <= 5):
            self.shiny = True
        else:
            self.shiny = False