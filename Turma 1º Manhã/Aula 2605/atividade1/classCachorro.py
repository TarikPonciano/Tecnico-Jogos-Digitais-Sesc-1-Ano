class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        
    def latir(self):
        print(f"{self.nome} disse: Au Au Au!")