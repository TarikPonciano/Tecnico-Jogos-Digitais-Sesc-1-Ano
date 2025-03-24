# Crie um programa que pede nome de livros e os cadastra em uma lista, esse programa deve repetir até que a pessoa escreva um livro com nome "Sair" e deve apenas cadastrar livros que ainda não existem na lista.

livros = []

while(True):
    novoLivro = input("Digite o nome de um livro:")

    if (novoLivro == "Sair"):
        print("Finalizando programa!")
        break

    if (novoLivro in livros):
        print("LIVRO REPETIDO! DIGITE UM NOVO LIVRO")
    else:
        livros.append(novoLivro)

    print(livros)

print("BIBLIOTECA:")

for i in range(len(livros)):
    print(f"{i+1}. {livros[i]}")