# 2. Crie uma lista de animais e insira na lista 7 espécies de animais diferentes, depois imprima na tela. Bônus: Use repetições para inserir nomes na lista e ao exibir mostre como uma lista numerada. Ex:
#1. Animal X
#2. Animal Y
#3. Capivara

# animais = ["Jacaré", "Tatu", "Morcego", "Cachorro", "Aranha", "Jabuti", "Capivara"]

# print(animais)

animais = []

for i in range(7):
    novoAnimal = input("Digite uma nova espécie de animal: ")
    animais.append(novoAnimal)

for i in range(len(animais)):
    print(f"{i+1}. {animais[i]}")
