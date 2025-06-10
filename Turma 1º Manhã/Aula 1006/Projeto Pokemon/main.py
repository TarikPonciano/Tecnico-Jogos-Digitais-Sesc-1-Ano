from classPokemon import *
from classTreinador import *
import random

pokedex = {
     "Bulbasaur": {
        "nroPokedex": 1,
        "tipo": ["Grass", "Poison"],
        "hp": 45,
        "atk": 49,
        "defesa": 49
    },
    "Charmander": {
        "nroPokedex": 4,
        "tipo": ["Fire"],
        "hp": 39,
        "atk": 52,
        "defesa": 43
    },
    "Squirtle": {
        "nroPokedex": 7,
        "tipo": ["Water"],
        "hp": 44,
        "atk": 48,
        "defesa": 65
    },
    "Pikachu": {
        "nroPokedex": 25,
        "tipo": ["Electric"],
        "hp": 35,
        "atk": 55,
        "defesa": 40
    },
    "Jigglypuff": {
        "nroPokedex": 39,
        "tipo": ["Normal", "Fairy"],
        "hp": 115,
        "atk": 45,
        "defesa": 20
    },
    "Meowth": {
        "nroPokedex": 52,
        "tipo": ["Normal"],
        "hp": 40,
        "atk": 45,
        "defesa": 35
    },
    "Psyduck": {
        "nroPokedex": 54,
        "tipo": ["Water"],
        "hp": 50,
        "atk": 52,
        "defesa": 48
    },
    "Machop": {
        "nroPokedex": 66,
        "tipo": ["Fighting"],
        "hp": 70,
        "atk": 80,
        "defesa": 50
    },
    "Geodude": {
        "nroPokedex": 74,
        "tipo": ["Rock", "Ground"],
        "hp": 40,
        "atk": 80,
        "defesa": 100
    },
    "Gastly": {
        "nroPokedex": 92,
        "tipo": ["Ghost", "Poison"],
        "hp": 30,
        "atk": 35,
        "defesa": 30
    },
    "Onix": {
        "nroPokedex": 95,
        "tipo": ["Rock", "Ground"],
        "hp": 35,
        "atk": 45,
        "defesa": 160
    },
    "Magikarp": {
        "nroPokedex": 129,
        "tipo": ["Water"],
        "hp": 20,
        "atk": 10,
        "defesa": 55
    },
    "Eevee": {
        "nroPokedex": 133,
        "tipo": ["Normal"],
        "hp": 55,
        "atk": 55,
        "defesa": 50
    },
    "Snorlax": {
        "nroPokedex": 143,
        "tipo": ["Normal"],
        "hp": 160,
        "atk": 110,
        "defesa": 65
    },
    "Mewtwo": {
        "nroPokedex": 150,
        "tipo": ["Psychic"],
        "hp": 106,
        "atk": 110,
        "defesa": 90
    },
    "Chikorita": {
        "nroPokedex": 152,
        "tipo": ["Grass"],
        "hp": 45,
        "atk": 49,
        "defesa": 65
    },
    "Cyndaquil": {
        "nroPokedex": 155,
        "tipo": ["Fire"],
        "hp": 39,
        "atk": 52,
        "defesa": 43
    },
    "Totodile": {
        "nroPokedex": 158,
        "tipo": ["Water"],
        "hp": 50,
        "atk": 65,
        "defesa": 64
    },
    "Mareep": {
        "nroPokedex": 179,
        "tipo": ["Electric"],
        "hp": 55,
        "atk": 40,
        "defesa": 40
    },
    "Treecko": {
        "nroPokedex": 252,
        "tipo": ["Grass"],
        "hp": 40,
        "atk": 45,
        "defesa": 35
    }
}

def gerarPokemonAleatorio():
    nomePokemonAleatorio = random.choice(list(pokedex.keys()))
    dados = pokedex[nomePokemonAleatorio]

    pokemonAleatorio = Pokemon(nomePokemonAleatorio, dados["nroPokedex"], dados["tipo"], dados["hp"], dados["atk"], dados["defesa"])

    return pokemonAleatorio

def batalhaPokemon(meuPokemon, inimigo):
    hpInicial = meuPokemon.hp

    while (meuPokemon.hp > 0 and inimigo.hp > 0):

        meuPokemon.atacar(inimigo)

        if (inimigo.hp <= 0):
            print(f"{inimigo.especie} desmaiou!")
            print(f"{meuPokemon.especie} venceu a batalha!")
            meuPokemon.hp = hpInicial
            break

        inimigo.atacar(meuPokemon)

        if(meuPokemon.hp <= 0):
            print(f"{meuPokemon.especie} desmaiou!")
            print(f"{meuPokemon.especie} perdeu a batalha!")
            meuPokemon.hp = hpInicial
            break

jogador = Jogador("Tarik", [])

print("Seja bem vindo ao Mundo Pokemon!")
print("Para começar o jogo você deve escolher um pokemon inicial: ")

print(f'''

1. Charmander
2. Bulbausaur
3. Squirtle

''')

op = input("Digite o número do pokemon desejado: ")

pokemonInicial = Pokemon("Pikachu", 23, "Elétrico", 100, 30, 10)

if op == "1":
    pokemonInicial = PokemonFogo("Charmander", 3, 100, 20, 20)
elif op == "2":
    pokemonInicial = PokemonGrama("Bulbasaur", 5, 100, 20, 20)
elif op == "3":
    pokemonInicial = PokemonAgua("Squirtle", 7, 100, 20, 20)
else:
    print("Esse pokemon não está mais disponível! Você ficará com um Pikachu!")

jogador.capturarPokemon(pokemonInicial)

while True:

    print('''
O que deseja fazer agora?
          
Menu:
          
    1. Capturar Pokemon Aleatório
    2. Batalhar contra Pokemon Aleatório
    3. Ver Pokemons
    4. Pescar Pokemon
    0. Sair
        

''')
    
    op = input("Digite a opção desejada:")

    if (op == "1"):
        jogador.capturarPokemon(gerarPokemonAleatorio())
    elif (op == "2"):
        batalhaPokemon(jogador.escolherPokemon(), gerarPokemonAleatorio())
    elif (op == "3"):
        jogador.verPokemons()
    elif (op == "0"):
        print("Saindo do Programa...")
        break
    else:
        print("Escolha uma opção válida!")

    input("DIGITE ENTER PARA CONTINUAR!")