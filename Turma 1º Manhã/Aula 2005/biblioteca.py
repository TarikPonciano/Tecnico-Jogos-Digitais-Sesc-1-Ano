# Proponha 3 classes diferentes que poderiam ser usadas em um sistema de biblioteca. Identifique os atributos (pelo menos 3) de cada classe e implemente as 3 classes no código abaixo. Crie 1 objeto de cada classe.

class Livro():
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

class Usuario():
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Pagamento():
    def __init__(self, valor, tipo, livro):
        self.valor = valor
        self.tipo = tipo
        self.livro = livro


livro1 = Livro("Heróis da Fé", "Desconhecido", "Teologia")


usuario1 = Usuario("Arthur Rocha", "arthurrocha@gmail.com", "110609")

pagamento1 = Pagamento(50, "Pix", livro1)

print(pagamento1.livro.)

