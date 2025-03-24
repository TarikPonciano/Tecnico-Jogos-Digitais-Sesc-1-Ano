#  3. Crie um programa que pede nome de livros e os cadastra em uma lista, esse programa deve repetir até que a pessoa escreva um livro com nome "Sair" e deve apenas cadastrar livros que ainda não existem na lista.

livros = []


while True:
    novoLivro = input("Digite o nome de um livro: ")

    if novoLivro == "Sair":
        print("Encerrando o programa...")
        break
    
    if (novoLivro in livros):
        print("Livro já cadastrado! Digite um novo livro!")
    else:    
        livros.append(novoLivro)

for i in range(len(livros)):
    print(f"{i+1}. {livros[i]}")