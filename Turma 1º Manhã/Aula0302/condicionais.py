# Crie um programa que recebe a idade do usuário e determina se ele pode ou não assistir Jogos Mortais. Exiba na tela se ele está autorizado ou não.

# Exiba uma lista de 5 filmes, dependendo se a pessoa é maior ou menor de idade.

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você está autorizado!")
    print(f"Sua idade é: {idade} anos!")
    
else:
    print("Você não está autorizado!")
    print("Volte quando tiver 18 anos!")
    print("Escolha outro filme: ")
    print("1. Smurfs")
    print("2. Sonic 3")
    print("3. Wall-e")
    print("4. Jumanji")
    print("5. Transformers")

print("A família CineTarik agradece seu contato!")