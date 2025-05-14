import classPokemon
# Crie uma mensagem que exibe na tela "Seja bem vindo ao mundo Pokemon"
pokedex = {
    1: {"nome": "Bulbassauro", "hp": 50, "atk": 20}
}

nomeJogador = ""
pokemonInicialJogador = {}

nomeRival = ""
pokemonInicialRival = {
    "nome": "",
    "level": 1,
    "hp": 0,
    "atk": 0
}

print("Seja bem vindo ao mundo Pokemon!")

# Crie um dialogo com o professor pokemon onde ele pergunta seu nome e se apresenta

print("Olá jovem treinador, meu nome é Prof. Carvalho. Como posso lhe chamar?")

nomeJogador = input("Digite seu nome: ")

print(f"Olá {nomeJogador}, esse é um belo nome! Tenho certeza que você conquistará grandes coisas. Você deve conhecer o meu neto. Qual era o nome dele mesmo?")

nomeRival = input("Digite o nome do seu rival: ")

# Exiba uma lista contendo os pokemons iniciais (3 pokemons) e peça para o jogador escolher o seu pokemon favorito

print(f"Prof. Carvalho: Ah isso mesmo! {nomeRival} é o nome dele mesmo. Espero que vocês se dêem bem. Agora vamos para o que o você veio fazer aqui. Escolha seu primeiro parceiro pokemon!")

while pokemonInicialJogador == {}:

    print('''
    Escolha um dos pokemons abaixo:
            1. Bulbassauro
            2. Charmander
            3. Squirtle

    ''')

    op = int(input("Digite o número de um dos pokemons: "))

    if (op == 1):
        pokemonInicialJogador = pokedex[1]
        pokemonInicialJogador["level"] = 1

        pokemonInicialRival["nome"] = "Charmander"
        pokemonInicialRival["hp"] = 40
        pokemonInicialRival["level"] = 1
        pokemonInicialRival["atk"] = 30

    elif (op == 2):
        pokemonInicialJogador["nome"]= "Charmander"
        pokemonInicialJogador["hp"] = 40
        pokemonInicialJogador["level"] = 1
        pokemonInicialJogador["atk"] = 30

        pokemonInicialRival["nome"] = "Squirtle"
        pokemonInicialRival["hp"] = 60
        pokemonInicialRival["level"] = 1
        pokemonInicialRival["atk"] = 10
    elif (op == 3):
        pokemonInicialJogador["nome"]= "Squirtle"
        pokemonInicialJogador["hp"] = 60
        pokemonInicialJogador["level"] = 1
        pokemonInicialJogador["atk"] = 10

        pokemonInicialRival["nome"] = "Bulbassauro"
        pokemonInicialRival["hp"] = 50
        pokemonInicialRival["level"] = 1
        pokemonInicialRival["atk"] = 20

    else:
        print("Escolha um pokemon válido!")

# Determine agora o pokemon do rival. Crie um dicionário para guardar as informações dele e atribua as informações do pokemon, como foi feito com o pokemon do jogador.

print("Pokemon escolhido pelo jogador: ", pokemonInicialJogador)

print("Pokemon escolhido pelo rival: ", pokemonInicialRival)

while pokemonInicialJogador["hp"]>0 and pokemonInicialRival["hp"]>0:

    print(f"{pokemonInicialJogador['nome']} atacou e causou {pokemonInicialJogador['atk']} de dano!")

    pokemonInicialRival["hp"] -= pokemonInicialJogador["atk"]

    print(f"Vida restante do {pokemonInicialRival['nome']} é {pokemonInicialRival['hp']}")

    if (pokemonInicialRival["hp"] <= 0):
        print(f"{pokemonInicialRival['nome']} desmaiou")
        break

    print(f"{pokemonInicialRival['nome']} atacou e causou {pokemonInicialRival['atk']}!")

    pokemonInicialJogador["hp"] -= pokemonInicialRival["atk"]

    print(f"Vida restante do {pokemonInicialJogador['nome']} é { pokemonInicialJogador['hp']}!")
    if pokemonInicialJogador["hp"] <= 0:
        print(f"{pokemonInicialJogador['nome']} desmaiou!")
        break