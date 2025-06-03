class Animal:
    def __init__(self, nome, peso, idade, som):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.som = som
    def comer(self):
        print(f"{self.nome} está comendo!")
    def beber(self):
        print(f"{self.nome} está bebendo!")
    def fazerSom(self):
        print(f"{self.nome} disse: {self.som}")
    


class Cachorro(Animal):
    def __init__(self, nome, peso, idade):
        super().__init__(nome, peso, idade, "Au Au Au")
    def calcularImpostos(self):
        print("Au au au")

class Gato(Animal):
    def __init__(self, nome, peso, idade):
        super().__init__(nome, peso, idade, "Miau Miau Miau")
    def fazerSom(self):
        print(f"{self.nome} disse: MiAu MiAu MiAu")

class Coelho(Animal):
    def __init__(self, nome, peso, idade):
        super().__init__(nome, peso, idade, "Sniff Sniff Sniff")

class Papagaio(Animal):
    def __init__(self, nome, peso, idade):
        super().__init__(nome, peso, idade, "Lôro quer biscoito")

class Tartaruga(Animal):
    def __init__(self, nome, peso, idade):
        super().__init__(nome, peso, idade, "AAAAAAAAAAAAAANNNNNNNnnn")