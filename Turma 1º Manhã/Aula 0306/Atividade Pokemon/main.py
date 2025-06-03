from classPokemon import Pokemon
from classTreinador import Treinador

jogador = Treinador("Tarik", [Pokemon("Lugia", "Psíquico", 50)])

poke1 = Pokemon("Charmander", "Fogo", 1)
poke2 = Pokemon("Bulbasaur", "Grama", 1)
poke3 = Pokemon("Squirtle", "Água", 1)

print("Bem vindo ao mundo Pokemon!")

print("Escolha seu primeiro parceiro nessa aventura: ")

print('''
      
Pokemons Disponíveis:
      
1. Charmander
2. Bulbasaur
3. Squirtle
      
''')

op = input("Digite o número do pokemon desejado:")

if op == "1":
    jogador.pokemons.append(poke1)
elif op == "2":
    jogador.pokemons.append(poke2)
elif op == "3":
    jogador.pokemons.append(poke3)
else:
    print("Você escolheu um pokemon inválido! Você receberá o Charmander!")
    jogador.pokemons.append(poke1)

jogador.mostrarPokemons()