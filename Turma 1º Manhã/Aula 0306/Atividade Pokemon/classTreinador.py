class Treinador:
    def __init__(self, nome, pokemons):
        self.nome = nome
        self.pokemons = pokemons
    def mostrarPokemons(self):
        for pokemon in self.pokemons:
            pokemon.mostrarInformacoes()