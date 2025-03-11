# Crie uma lista que guarda o nome de frutas
frutas = []
# Peça que o usuário escreva o nome de 5 frutas e adicione-as à lista
for i in range(5):
    fruta = input("Digite o nome de uma fruta: ")
    frutas.append(fruta)

# Após escrever o nome das frutas exiba o nome dela no terminal
print(frutas)

contador = 1
for fruta in frutas:
    print(f"{contador}. {fruta}")
    contador += 1
    
# Exiba na tela apenas as frutas que começam com a letra A