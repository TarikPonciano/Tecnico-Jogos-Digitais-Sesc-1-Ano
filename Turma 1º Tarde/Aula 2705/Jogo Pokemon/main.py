from classPokemon import Pokemon

def batalhaPokemonV1(pk1, pk2):

    poderPk1 = pk1.hp + pk1.atk + pk1.defesa
    poderPk2 = pk2.hp + pk2.atk + pk2.defesa

    print(f"BATALHA INICIADA")
    print()
    print(f'''
{pk1.especie} - {poderPk1} pontos de poder 
                    X 
{pk2.especie} - {poderPk2} pontos de poder''')
    print()
    print("-----------------------------------")

    if poderPk1 > poderPk2:
        print(f"O vencedor da batalha foi o {pk1.especie}!")
    elif poderPk2 > poderPk1:
        print(f"O vencedor da batalha foi o {pk2.especie}!")
    else:
        print(f"A BATALHA TERMINOU EM EMPATE!")

def batalhaPokemonV2(pk1, pk2):

    print(f"BATALHA INICIADA")
    print()
    print(f'''
{pk1.especie} 
      X 
{pk2.especie} ''')
    print()
    print("-----------------------------------")

    while pk1.hp>0 and pk2.hp>0:
        print(f"----- Turno do {pk1.especie} -----")
        dano1 = int((pk1.atk/pk2.defesa) * 5)
        print(f"{pk1.especie} atacou causando {dano1} de dano!")
        print(f"{pk2.especie} sofreu {dano1} de dano!")
        pk2.hp -= dano1
        print(f"{pk2.especie} possui {pk2.hp} pontos de vida restante!")
        print()

        if(pk2.hp <= 0):
            print(f"{pk2.especie} desmaiou!")
            print(f"{pk1.especie} foi o vencedor do combate!")
            break

        print()
        print(f"----- Turno do {pk2.especie} -----")
        dano2 = int((pk2.atk/pk1.defesa) * 5)
        print(f"{pk2.especie} atacou causando {dano2} de dano!")
        print(f"{pk1.especie} sofreu {dano2} de dano!")
        pk1.hp -= dano2
        print(f"{pk1.especie} possui {pk1.hp} pontos de vida restante!")
        print()

        if(pk1.hp <= 0):
            print(f"{pk1.especie} desmaiou!")
            print(f"{pk2.especie} foi o vencedor do combate!")
            break
        




poke1 = Pokemon("Charmander", "Fogo", 39, 52, 43)

print(f'''
----- Registro Pokemon -----

      Espécie: {poke1.especie}
      Tipo: {poke1.tipo}
      HP: {poke1.hp}
      ATK: {poke1.atk}
      DEF: {poke1.defesa}
''')

poke2 = Pokemon("Bulbasaur", "Grama", 45, 49, 49)

print(f'''
----- Registro Pokemon -----

      Espécie: {poke2.especie}
      Tipo: {poke2.tipo}
      HP: {poke2.hp}
      ATK: {poke2.atk}
      DEF: {poke2.defesa}
''')

# Criar um sistema de batalha que usa as informações dos dois pokemons e decide o vencedor.

batalhaPokemonV1(poke1, poke2)

batalhaPokemonV2(poke1, poke2)

print(f'''
----- Registro Pokemon -----

      Espécie: {poke2.especie}
      Tipo: {poke2.tipo}
      HP: {poke2.hp}
      ATK: {poke2.atk}
      DEF: {poke2.defesa}
''')