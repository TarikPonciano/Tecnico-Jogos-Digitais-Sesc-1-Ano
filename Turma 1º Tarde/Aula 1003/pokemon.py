# Crie um programa inspirado no jogo Pokemon
#  Você deverá criar as variáveis nomeTreinador, nomePokemon, tipoPokemon, poderPokemon
# Peça o nome de treinador para o jogador e guarde na variável adequada
# Ofereça uma lista de opções (pelo menos 3) de pokemons para que o jogador escolha. Ao escolher um pokemon preencha as variáveis nome, tipo e poder do Pokemon
# Simule uma batalha pokemon com um pokemon aleatório (verificar o maior poder) e imprima na tela quem venceu a batalha
import time
nomeTreinador = ""
nomePokemon = ""
tipoPokemon = ""
poderPokemon = 0
hpPokemon = 0



print("Bem vindo ao MUNDO POKEMON")
print()
print("Olá eu sou o Prof. Carvalho")
print("Qual o seu nome, pessoe?")
print()
nomeTreinador = input("Digite seu nome: ")
print()
print("Para iniciar sua aventura, você precisará de um companheiro!")
while(True):
    print('''
    Escolha um dos pokemons abaixo:
        1. Charmander
        2. Squirtle
        3. Bulbasauro  
        ''')

    op = input("Digite o número do pokemon desejado: ")

    if op == "1":
        nomePokemon = "Charmander"
        tipoPokemon = "Fogo"
        poderPokemon = 40
        hpPokemon = 120
        break
    elif op == "2":
        nomePokemon = "Squirtle"
        tipoPokemon = "Água"
        poderPokemon = 30
        hpPokemon = 160
        break
    elif op == "3":
        nomePokemon = "Bulbasauro"
        tipoPokemon = "Grama"
        poderPokemon = 20
        hpPokemon = 200
        break
    else:
        print("Você escolheu um número inválido! Tente novamente")

print(f"UAU Você escolheu o {nomePokemon} com {poderPokemon} de poder!")

nomePokemonInimigo = "Spearow"
tipoPokemonInimigo = "Normal"
poderPokemonInimigo = 30
hpPokemonInimigo = 150

print()
print(f"POKEMON ENCONTRADO NA GRAMA!")
print(f"UM {nomePokemonInimigo.upper()} SELVAGEM APARECEU!")
time.sleep(2)

while (hpPokemon > 0 and hpPokemonInimigo > 0):

    print(f"------------ TURNO DO {nomePokemon} -------------")
    print(f"O pokemon inimigo {nomePokemonInimigo} foi acertado pelo {nomePokemon}.")
    print(f"O {nomePokemonInimigo} tomou {poderPokemon} de dano!")
    hpPokemonInimigo -= poderPokemon
    print(f"HP RESTANTE DO {nomePokemonInimigo}: {hpPokemonInimigo}")

    time.sleep(1)


    if (hpPokemonInimigo > 0):
        print(f"------------ TURNO DO {nomePokemonInimigo} -------------")
        print(f"O pokemon {nomePokemon} foi acertado pelo {nomePokemonInimigo}.")
        print(f"O {nomePokemon} tomou {poderPokemonInimigo} de dano!")
        hpPokemon -= poderPokemonInimigo
        print(f"HP RESTANTE DO {nomePokemon}: {hpPokemon}")
        time.sleep(1)


time.sleep(2)
if (hpPokemon > hpPokemonInimigo):
    print(f"O pokemon inimigo desmaiou. Parabéns {nomePokemon} venceu!")
else:
    print(f"Seu pokemon desmaiou. Uma pena {nomePokemonInimigo} venceu!")