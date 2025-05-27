from classPokemon import Pokemon

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

