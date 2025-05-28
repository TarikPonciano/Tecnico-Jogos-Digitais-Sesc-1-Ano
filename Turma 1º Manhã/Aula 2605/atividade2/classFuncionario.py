class Funcionario:
    def __init__(self, nome, salario, cargo, idade, situacao):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        self.idade = idade
        self.situacao = situacao

    def aumentarSalario(self, aumento):
        if ((self.salario + aumento) >= 20000):
            self.salario = 20000
            print("TETO SALARIAL ALCANÇADO!")
        else:
            self.salario = self.salario + aumento

    def reduzirSalario(self, reducao):
        if ((self.salario - reducao) <= 1518):
            self.salario = 1518
        else:
            self.salario = self.salario - reducao

    def mostrarInformacoes(self):
        print(f'''
----- Informações do Funcionário -----
              
    Nome: {self.nome}
    Salário: R$ {self.salario:.2f}
    Cargo: {self.cargo}
    Idade: {self.idade} anos
    Situação: {"Ativo" if self.situacao==True else "Inativo"}
''')