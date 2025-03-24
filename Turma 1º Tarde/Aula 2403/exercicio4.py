# 4. Crie uma lista com nomes de pokemon, faça um programa que exibe na tela a mensagem "Um {pokemon} selvagem apareceu!". O pokemon deve ser escolhido de forma aleatória.
import random
import time
pokemons = ["Charmander", "Pikachu", "Bulbassauro","Charizard", "Onyx", "JigglyPuff", "Eevee", "Mewtwo", "Gengar"]

pokemonEscolhido1 = random.choice(pokemons)
pokemonEscolhido2 = pokemons[random.randint(0, 
 len(pokemons) - 1)]


print(f"Um {pokemonEscolhido1} selvagem apareceu!")
time.sleep(3)

print(f"Você escolheu o {pokemonEscolhido2} para batalhar!")
time.sleep(3)

vitoria = random.randint(0,100)

time.sleep(3)
if vitoria <50:
    print(f"{pokemonEscolhido1} venceu! Você foi derrotado")
else: 
    print(f"{pokemonEscolhido2} venceu! Você venceu!")

