# Crie as variáveis nomeTreinador, nomePokemon, poderPokemon, tipoPokemon
# Pergunte o nome do treinador e ofereça 3 opções de pokemon. Altere o valor das variáveis de acordo com o que foi escolhido.
# Crie uma batalha simples entre o pokemon escolhido e um outro pokemon e verifique qual possui maior poder de batalha. Imprima o vencedor da batalha na tela.

nomeTreinador = ""
nomePokemon = ""
tipoPokemon = ""
poderPokemon = 0

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
        break
    elif (op == "2"):
        nomePokemon = "Squirtle"
        tipoPokemon = "Água"
        poderPokemon = 100
        break
    elif (op == "3"):
        nomePokemon = "Bulbasauro"
        tipoPokemon = "Grama"
        poderPokemon = 100
        break
    else:
        print("Você escolheu um pokemon inválido!")

print(f"Parabéns você escolheu o {nomePokemon}!")

nomePokemonInimigo = "Spearow"
tipoPokemonInimigo = "Normal"
poderPokemonInimigo = 120
print("Pokemon encontrado na grama!")
print(f"Um {nomePokemonInimigo} selvagem apareceu!")

if (poderPokemon > poderPokemonInimigo):
    print(f"O pokemon vitorioso foi {nomePokemon}!")
elif (poderPokemon < poderPokemonInimigo):
    print(f"O pokemon vitorioso foi {nomePokemonInimigo}")