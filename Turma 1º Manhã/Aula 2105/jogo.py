#import classPokemon Maneira básica
from classPokemon import Pokemon

def batalhaV1(pokemon1, pokemon2):
    poderPokemon1 = pokemon1.atk + pokemon1.defesa + pokemon1.hp

    poderPokemon2 = pokemon2.atk + pokemon2.defesa + pokemon2.hp

    print(f"{pokemon1.especie} - {poderPokemon1} pontos de batalha")
    print()
    print("-----VERSUS-----")
    print()
    print(f"{pokemon2.especie} - {poderPokemon2} pontos de batalha")

    print()
    print("------RESULTADO DA BATALHA------")
    print()
    if (poderPokemon1 > poderPokemon2):
        print(f"{pokemon1.especie} venceu o {pokemon2.especie}!")
    elif (poderPokemon2 > poderPokemon1):
        print(f"{pokemon2.especie} venceu o {pokemon1.especie}!")
    else:
        print("EMPATE ENTRE OS POKEMONS!")


def batalhaV2(pokemon1, pokemon2):
    print(f"-----BATALHA INICIADA-----")
    print(f"{pokemon1.especie} VERSUS {pokemon2.especie}")
    print()

    while (True):

        dano1 = int((pokemon1.atk/pokemon2.defesa) * 10)
        print()
        print(f"{pokemon1.especie} atacou causando {dano1} de dano!")
        print()
        pokemon2.hp -= dano1
        print(f"{pokemon2.especie} está com {pokemon2.hp} restante")
        if (pokemon2.hp <= 0):
            print(f"{pokemon2.especie} DESMAIOU!")
            break
        
        dano2 = int((pokemon2.atk/pokemon1.defesa) * 10)

        print()
        print(f"{pokemon2.especie} atacou causando {dano2} de dano!")
        print()
        pokemon1.hp -= dano2
        print(f"{pokemon1.especie} está com {pokemon1.hp} restante")

        if (pokemon1.hp <= 0):
            print(f"{pokemon1.especie} DESMAIOU!")
            break

    if (pokemon1.hp > pokemon2.hp):
        print(f"O VENCEDOR DA BATALHA FOI {pokemon1.especie}")
    else: 
        print(f"O VENCEDOR DA BATALHA FOI {pokemon2.especie}")


poke1 = Pokemon("Charmander", "Fogo", 100, 50, 200)

print(f"{poke1.especie} - {poke1.tipo} - {poke1.shiny}")

poke2 = Pokemon("Squirtle", "Água", 80, 70, 250)

print(f"{poke2.especie} - {poke2.tipo} - {poke2.shiny}")

batalhaV2(poke1, poke2)

batalhaV2(poke1, poke2)
