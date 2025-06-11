from classPokemon import *
from classTreinador import *
import random

def batalhaPokemon(meuPokemon, inimigo):
    print("----- BATALHA INICIADA -----")

    print(f"{meuPokemon.especie} X {inimigo.especie}")
    print()
    turnos = 1
    
    hpMax = meuPokemon.hp
    
    while (meuPokemon.hp > 0 and inimigo.hp > 0):
        print(f"----- TURNO {turnos} -----")
        meuPokemon.atacar(inimigo)

        if (inimigo.hp <= 0):
            print(f"{inimigo.especie} desmaiou!")
            print(f"{meuPokemon.especie} venceu a batalha contra {inimigo.especie}")
            meuPokemon.hp = hpMax
            break
        
        inimigo.atacar(meuPokemon)

        if (meuPokemon.hp <= 0):
            print(f"{meuPokemon.especie} desmaiou!")
            print(f"{inimigo.especie} venceu a batalha contra {meuPokemon.especie}")
            meuPokemon.hp = hpMax
            break
        turnos += 1

def gerarPokemonAleatorio():
    numeroPokedex = random.randint(1, 30)

    dados = pokedex[numeroPokedex]

    pokemonAleatorio = Pokemon(numeroPokedex, dados["especie"], dados["tipo"], dados["hp"], dados["atk"], dados["defesa"])
    print("VOCÊ ENCONTROU UM POKEMON!")
    pokemonAleatorio.mostrarInformacoes()
    return pokemonAleatorio

pokedex = {
    1:  {"especie": "Bulbasaur",    "tipo": "Grama/Veneno", "hp": 45,  "atk": 49,  "defesa": 49},
    2:  {"especie": "Ivysaur",      "tipo": "Grama/Veneno", "hp": 60,  "atk": 62,  "defesa": 63},
    3:  {"especie": "Venusaur",     "tipo": "Grama/Veneno", "hp": 80,  "atk": 82,  "defesa": 83},
    4:  {"especie": "Charmander",   "tipo": "Fogo",         "hp": 39,  "atk": 52,  "defesa": 43},
    5:  {"especie": "Charmeleon",   "tipo": "Fogo",         "hp": 58,  "atk": 64,  "defesa": 58},
    6:  {"especie": "Charizard",    "tipo": "Fogo/Voador",  "hp": 78,  "atk": 84,  "defesa": 78},
    7:  {"especie": "Squirtle",     "tipo": "Água",         "hp": 44,  "atk": 48,  "defesa": 65},
    8:  {"especie": "Wartortle",    "tipo": "Água",         "hp": 59,  "atk": 63,  "defesa": 80},
    9:  {"especie": "Blastoise",    "tipo": "Água",         "hp": 79,  "atk": 83,  "defesa": 100},
    10: {"especie": "Caterpie",     "tipo": "Inseto",       "hp": 45,  "atk": 30,  "defesa": 35},
    11: {"especie": "Metapod",      "tipo": "Inseto",       "hp": 50,  "atk": 20,  "defesa": 55},
    12: {"especie": "Butterfree",   "tipo": "Inseto/Voador","hp": 60,  "atk": 45,  "defesa": 50},
    13: {"especie": "Weedle",       "tipo": "Inseto/Veneno","hp": 40,  "atk": 35,  "defesa": 30},
    14: {"especie": "Kakuna",       "tipo": "Inseto/Veneno","hp": 45,  "atk": 25,  "defesa": 50},
    15: {"especie": "Beedrill",     "tipo": "Inseto/Veneno","hp": 65,  "atk": 90,  "defesa": 40},
    16: {"especie": "Pidgey",       "tipo": "Normal/Voador","hp": 40,  "atk": 45,  "defesa": 40},
    17: {"especie": "Pidgeotto",    "tipo": "Normal/Voador","hp": 63,  "atk": 60,  "defesa": 55},
    18: {"especie": "Pidgeot",      "tipo": "Normal/Voador","hp": 83,  "atk": 80,  "defesa": 75},
    19: {"especie": "Rattata",      "tipo": "Normal",       "hp": 30,  "atk": 56,  "defesa": 35},
    20: {"especie": "Raticate",     "tipo": "Normal",       "hp": 55,  "atk": 81,  "defesa": 60},
    21: {"especie": "Spearow",      "tipo": "Normal/Voador","hp": 40,  "atk": 60,  "defesa": 30},
    22: {"especie": "Fearow",       "tipo": "Normal/Voador","hp": 65,  "atk": 90,  "defesa": 65},
    23: {"especie": "Ekans",        "tipo": "Veneno",       "hp": 35,  "atk": 60,  "defesa": 44},
    24: {"especie": "Arbok",        "tipo": "Veneno",       "hp": 60,  "atk": 85,  "defesa": 69},
    25: {"especie": "Pikachu",      "tipo": "Elétrico",     "hp": 35,  "atk": 55,  "defesa": 40},
    26: {"especie": "Raichu",       "tipo": "Elétrico",     "hp": 60,  "atk": 90,  "defesa": 55},
    27: {"especie": "Sandshrew",    "tipo": "Terra",        "hp": 50,  "atk": 75,  "defesa": 85},
    28: {"especie": "Sandslash",    "tipo": "Terra",        "hp": 75,  "atk": 100, "defesa": 110},
    29: {"especie": "Nidoran♀",     "tipo": "Veneno",       "hp": 55,  "atk": 47,  "defesa": 52},
    30: {"especie": "Nidorina",     "tipo": "Veneno",       "hp": 70,  "atk": 62,  "defesa": 67},
}

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
        jogador.capturarPokemon(gerarPokemonAleatorio())
    elif op == "2":
        batalhaPokemon(jogador.escolherPokemon(), gerarPokemonAleatorio())
    elif op == "3":
        jogador.verPokemons()
    elif op == "0":
        print("Você acorda do coma... Foi tudo um sonho... FIM DE JOGO")
        break
    else:
        print("Escolha uma opção válida!")

    input("DIGITE ENTER PARA CONTINUAR")


