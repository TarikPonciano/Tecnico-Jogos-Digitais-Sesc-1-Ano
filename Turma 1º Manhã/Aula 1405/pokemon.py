# Crie uma mensagem que exibe na tela "Seja bem vindo ao mundo Pokemon"
nomeJogador = ""
pokemonInicialJogador = {
    "nome": "",
    "level": 1,
    "hp": 0,
    "atk": 0
}


nomeRival = ""

print("Seja bem vindo ao mundo Pokemon!")

# Crie um dialogo com o professor pokemon onde ele pergunta seu nome e se apresenta

print("Olá jovem treinador, meu nome é Prof. Carvalho. Como posso lhe chamar?")

nomeJogador = input("Digite seu nome: ")

print(f"Olá {nomeJogador}, esse é um belo nome! Tenho certeza que você conquistará grandes coisas. Você deve conhecer o meu neto. Qual era o nome dele mesmo?")

nomeRival = input("Digite o nome do seu rival: ")

# Exiba uma lista contendo os pokemons iniciais (3 pokemons) e peça para o jogador escolher o seu pokemon favorito

print(f"Prof. Carvalho: Ah isso mesmo! {nomeRival} é o nome dele mesmo. Espero que vocês se dêem bem. Agora vamos para o que o você veio fazer aqui. Escolha seu primeiro parceiro pokemon!")

while pokemonInicialJogador == "":

    print('''
    Escolha um dos pokemons abaixo:
            1. Bulbassauro
            2. Charmander
            3. Squirtle

    ''')

    op = int(input("Digite o número de um dos pokemons: "))

    if (op == 1):
        pokemonInicialJogador["nome"] = "Bulbassauro"
        pokemonInicialJogador["hp"] = 50
        pokemonInicialJogador["level"] = 1
        pokemonInicialJogador["atk"] = 20
    elif (op == 2):
        pokemonInicialJogador["nome"]= "Charmander"
        pokemonInicialJogador["hp"] = 40
        pokemonInicialJogador["level"] = 1
        pokemonInicialJogador["atk"] = 30
    elif (op == 3):
        pokemonInicialJogador["nome"]= "Squirtle"
        pokemonInicialJogador["hp"] = 60
        pokemonInicialJogador["level"] = 1
        pokemonInicialJogador["atk"] = 10

    else:
        print("Escolha um pokemon válido!")
