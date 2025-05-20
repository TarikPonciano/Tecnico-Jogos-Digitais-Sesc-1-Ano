class Pessoa():
    def __init__(self, nomeParametro, idadeParametro, alturaParametro, pesoParametro):
        self.nome = nomeParametro

        if (idadeParametro >= 0):
            self.idade = idadeParametro
        else:
            self.idade = 0

        self.altura = alturaParametro
        self.peso = pesoParametro

        if (self.idade>=0 and self.idade <= 18):
            self.faixaEtaria = "Jovem"
        elif (self.idade>18 and self.idade <= 60):
            self.faixaEtaria = "Adulto"
        else:
            self.faixaEtaria = "Idoso"

    def mostrarInformacoes(self):
        print(f'''
Informações Pessoais:

Nome: {self.nome}
Idade: {self.idade} anos
Faixa Etária: {self.faixaEtaria}
Altura: {self.altura}m
Peso: {self.peso}kg
''')
