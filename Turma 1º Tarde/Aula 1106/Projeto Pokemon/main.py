from classPokemon import *
from classTreinador import *

jogador = Jogador("Tarik", [])

print("Bem vindo ao mundo Pokemon!")

print("Para começar sua jornada você precisa de um parceiro!")

print()

print('''Escolha um Pokemon abaixo:
      
      
1. Charmander
2. Bulbasaur
3. Squirtle
      
''')

op = input("Digite o número do pokemon desejado: ")

if op == "1":
    pokemonInicial = Pokemon(4,"Charmander", "Fogo", 120, 20, 20)
elif op == "2":
    pokemonInicial = Pokemon(1, "Bulbasaur", "Grama", 100, 20, 20)
elif op == "3":
    pokemonInicial = Pokemon(7, "Squirtle", "Água", 100, 20, 20)
else:
    pokemonInicial = Pokemon(25, "Pikachu", "Elétrico", 100, 20, 20)
    print("Infelizmente esse pokemon não está mais disponível. Você receberá um Pikachu!")

jogador.capturarPokemon(pokemonInicial)

while True:
    print('''
Escolha uma opção do menu abaixo:
          
          1. Capturar Pokemon Aleatório
          2. Batalhar contra Pokemon Aleatório
          3. Ver Pokemons Capturados
          0. Sair

''')
    op = input("Digite a opção desejada: ")

    if op == "1":
        print("Capturar Pokemon")
    elif op == "2":
        print("Batalha Pokemon")
    elif op == "3":
        jogador.verPokemons()
    elif op == "0":
        print("Você acorda do coma... Foi tudo um sonho... FIM DE JOGO")
        break
    else:
        print("Escolha uma opção válida!")

    input("DIGITE ENTER PARA CONTINUAR")


