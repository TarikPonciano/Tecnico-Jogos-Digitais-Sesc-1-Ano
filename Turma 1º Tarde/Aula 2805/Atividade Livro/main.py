from classLivro import Livro

livro1 = Livro("Senhor dos Anéis", "Tolkien", "Fantasia Medieval", True)
livro2 = Livro("O Príncipe", "Maquiavel", "Auto-Ajuda", True)
livro3 = Livro("A morte de Ivan Ilich", "Tolstói", "Drama", False)

livro1.alugar()
livro2.alugar()
livro3.alugar()
livro1.alugar()

# livros = []
# livros.append(livro1)
# livros.append(livro2)
# livros.append(livro3)

# while True:
#     print(f'''
#     Escolha um livro abaixo:
        
#             1. {livro1.titulo}
#             2. {livro2.titulo}
#             3. {livro3.titulo}

#     ''')

#     op = int(input("Digite o número do livro desejado: "))
#     livroEscolhido = None
#     if (op == 1):
#         livroEscolhido = livro1
#         livro1.mostrarInformacoes()
#     elif (op == 2):
#         livroEscolhido = livro2
#         livro2.mostrarInformacoes()
#     elif (op == 3): 
#         livroEscolhido = livro3
#         livro3.mostrarInformacoes()
#     else: 
        
#         print("Escolha um livro válido!")

#     if livroEscolhido != None:
#         print("Deseja alugar esse livro?")
#         decisao = input("SIM OU NÃO:")

#         if(decisao == "SIM"):
#             livroEscolhido.alugar()
#     input()
