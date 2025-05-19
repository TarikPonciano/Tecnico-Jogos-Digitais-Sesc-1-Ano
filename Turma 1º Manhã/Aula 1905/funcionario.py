class Funcionario():
    def __init__(self, nome, cargo, salario, cpf):

        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.cpf = cpf

    def aumento(self, novoSalario):
        self.salario = novoSalario