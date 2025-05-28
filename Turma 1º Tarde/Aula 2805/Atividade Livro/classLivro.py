class Livro:
    def __init__(self, titulo, autor, genero, disponibilidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponibilidade = disponibilidade

    def mostrarInformacoes(self):

        print(f'''
----- Informações do Livro -----
              
    Título: {self.titulo}
    Autor: {self.autor}
    Genero: {self.genero}
    Disponibilidade: {"Disponível" if self.disponibilidade == True else "Indisponível"}
''')
    def alugar(self):
        if (self.disponibilidade == True):
            self.disponibilidade = False
            print(f"Livro {self.titulo} foi alugado com sucesso!")
        else:
            print(f"Não é possível alugar o livro {self.titulo}!")