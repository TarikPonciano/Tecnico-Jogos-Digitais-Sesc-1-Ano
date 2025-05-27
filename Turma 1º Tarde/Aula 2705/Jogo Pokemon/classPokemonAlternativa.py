from pokedex import pokedex_kanto

class Pokemon:
    def __init__(self, especie):
        self.especie = especie
        self.tipo = pokedex_kanto[especie]["tipo"]
        self.hp = pokedex_kanto[especie]["hp"]
        self.atk = pokedex_kanto[especie]["atk"]
        self.defesa = pokedex_kanto[especie]["defesa"]
        self.frutaPreferida = "Manga"
        self.vantagens = []
        if "Elétrico" in self.tipo:
            self.vantagens = ["Água", "Voador"]
        elif "Fogo" in self.tipo:
            self.vantagens = ["Grama", "Inseto"]



poke1 = Pokemon("Jigglypuff")

print(poke1.especie,poke1.tipo,poke1.atk,poke1.defesa,poke1.hp, poke1.frutaPreferida, poke1.vantagens)