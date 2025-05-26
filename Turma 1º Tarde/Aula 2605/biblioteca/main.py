#import classLivro Maneira 1

#livro1 = classLivro.Livro() Maneira 1

from classLivro import Livro

titulo = input("Digite o titulo do livro: ")
nroPaginas = int(input("Digite quantas páginas possui o livro:"))
genero = input("Digite o genero do livro:")
autor = input("Digite o nome do autor: ")
anoLancamento = int(input("Digite o ano de lançamento: "))

livro1 = Livro(titulo, nroPaginas, genero, autor, anoLancamento)

print(f'''
----- Informações do Livro -----

      Título: {livro1.titulo}
      Numero de Páginas: {livro1.nroPaginas} paginas
      Genero: {livro1.genero}
      Autor: {livro1.autor}
      Ano de Lançamento: {livro1.anoLancamento}
 
''')