animais = []

while True:
    animal = input("Digite o nome de um animal: ")
    if (animal == "Sair"):
        print("Encerrando programa...")
        break

    animais.append(animal)

print("Lista de Animais:")

animais.sort()

contador = 1
for animal in animais:
    print(f"{contador}. {animal}")
    contador += 1



