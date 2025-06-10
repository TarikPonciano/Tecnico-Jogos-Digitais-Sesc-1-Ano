class Treinador:
    def __init__(self, nome, pokemons):
        self.nome = nome
        self.pokemons = pokemons
    def mostrarInformacoes(self):
        print(f'''
----- Informações do Treinador -----
              
Nome: {self.nome}
Quantidade de Pokemons: {len(self.pokemons)}

''')
    def verPokemons(self):
        if (len(self.pokemons) > 0):
            print("Lista de Pokemons:")
            for i, pokemon in enumerate(self.pokemons):
                print(f"{i+1}. {pokemon.especie}")

            op = int(input("Digite o número do pokemon que deseja ver detalhes: "))

            self.pokemons[op-1].mostrarInformacoes()
        else:
            print("Você não possui pokemons!")
    

class Jogador(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)
    def capturarPokemon(self, pokemon):

        self.pokemons.append(pokemon)
        print(f"Você capturou um {pokemon.especie}!")

class Inimigo(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)
