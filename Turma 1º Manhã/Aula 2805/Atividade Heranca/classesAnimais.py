class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def comer(self):
        print(f"O(A) {self.nome} está comendo!")
        
class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)