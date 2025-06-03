class Pet:
    def __init__(self, nome, tipo, idade):
        self.__nome = nome
        self.tipo = tipo
        self.idade = idade
        self.vacinas = []

    def vacinar(self, novaVacina):
        if (novaVacina in self.vacinas):
            print("O pet já tomou essa vacina!")
        else:
            self.vacinas.append(novaVacina)
            print(f"{self.__nome} tomou a vacina {novaVacina}!")

    def envelhecer(self):
        self.idade += 1
        print(f"{self.__nome} fez aniversário e agora tem {self.idade} anos!")

    def mostrarInformacoes(self):

        print(f'''
Nome: {self.__nome}
Idade: {self.idade}
Tipo: {self.tipo}
Vacinas: {self.vacinas}
''')
    def getNome(self):
        return self.__nome
    def setNome(self, novoNome):
        if len(novoNome) >= 6:
            self.__nome = novoNome