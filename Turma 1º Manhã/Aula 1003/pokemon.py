# Crie as variáveis nomeTreinador, nomePokemon, poderPokemon, tipoPokemon
# Pergunte o nome do treinador e ofereça 3 opções de pokemon. Altere o valor das variáveis de acordo com o que foi escolhido.
# Crie uma batalha simples entre o pokemon escolhido e um outro pokemon e verifique qual possui maior poder de batalha. Imprima o vencedor da batalha na tela.
# Inclua agora nos dois pokemons as variáveis hp e ataque
# Faça com que a batalha dure até que um dos pokemons fique sem hp, então imprima o resultado na tela
# Melhore a batalha para exibir cada turno da batalha, quanto de dano foi sofrido e o hp restante de cada pokemon
import time
import random

nomeTreinador = ""
nomePokemon = ""
tipoPokemon = ""
poderPokemon = 0
hpPokemon = 0
atkPokemon = 0




print("Seja bem vindo ao mundo Pokemon!")
print("Meu nome é professor Carvalho e serei seu guia nessa aventura!")

print("Como posso lhe chamar?")

nomeTreinador = input("Digite seu nome:")

print(f"É um prazer lhe conhecer {nomeTreinador}!")

while (True):
    print("Agora escolha seu primeiro pokemon:")
    print('''
    1. Charmander
    2. Squirtle
    3. Bulbasauro
    ''')
    op = input("Digite o número do pokemon desejado: ")

    if (op == "1"):
        nomePokemon = "Charmander"
        tipoPokemon = "Fogo"
        poderPokemon = 100
        atkPokemon = 20
        hpPokemon = 60
        break
    elif (op == "2"):
        nomePokemon = "Squirtle"
        tipoPokemon = "Água"
        poderPokemon = 100
        atkPokemon = 15
        hpPokemon = 80
        break
    elif (op == "3"):
        nomePokemon = "Bulbasauro"
        tipoPokemon = "Grama"
        poderPokemon = 100
        atkPokemon = 10
        hpPokemon = 100
        break
    else:
        print("Você escolheu um pokemon inválido!")

print(f"Parabéns você escolheu o {nomePokemon}! Ele tem {poderPokemon} de força!")

nomePokemonInimigo = "Spearow"
tipoPokemonInimigo = "Normal"
poderPokemonInimigo = 120
hpPokemonInimigo = 100
atkPokemonInimigo = 20

print("Pokemon encontrado na grama!")
print(f"Um {nomePokemonInimigo} selvagem apareceu!")
turnos = 1
while(hpPokemon > 0 and hpPokemonInimigo > 0):
    print()
    print(f"############### Turno {turnos}###############")
    print()

    print(f"Turno do {nomePokemon}")
    print()

    time.sleep(1)

    turnos += 1
    print(f"{nomePokemonInimigo} foi atingido por um golpe de {nomePokemon}!")
    time.sleep(0.5)
    danoPokemon = int(atkPokemon * (random.randint(50,120)/100.0))
    if danoPokemon > atkPokemon:
        print(f"{nomePokemonInimigo} sofreu um golpe crítico e tomou {danoPokemon} de dano!")
    else:
        print(f"{nomePokemonInimigo} sofreu {danoPokemon} de dano!")
    time.sleep(0.5)
    hpPokemonInimigo -= danoPokemon
    print(f"HP restante do {nomePokemonInimigo}: {hpPokemonInimigo}")

    time.sleep(1)

    if (hpPokemonInimigo > 0):
        print(f"Turno do {nomePokemonInimigo}")
        print()
        print(f"{nomePokemon} foi atingido por um golpe de {nomePokemonInimigo}!")
        time.sleep(0.5)
        danoPokemonInimigo = int(atkPokemonInimigo * (random.randint(50,120)/100.0))

        if danoPokemonInimigo > atkPokemonInimigo:
            print(f"{nomePokemon} sofreu um golpe crítico e tomou {danoPokemonInimigo} de dano!")
        else:
            print(f"{nomePokemon} sofreu {danoPokemonInimigo} de dano!")

        time.sleep(0.5)
        hpPokemon -= danoPokemonInimigo
        print(f"HP restante do {nomePokemon}: {hpPokemon}")
        time.sleep(1)
    

if hpPokemon > 0:
    print(f"{nomePokemonInimigo} desmaiou!")
    print("Seu pokemon foi vitorioso!")
else:
    print(f"{nomePokemon} desmaiou!")
    print("Seu pokemon foi derrotado!")