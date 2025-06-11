class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    
    def comer(self):
        print(f"O {self.nome} está comendo!")
        
class Papagaio(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def comer(self):
        super().comer()
        print("Agora está ronronando")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)