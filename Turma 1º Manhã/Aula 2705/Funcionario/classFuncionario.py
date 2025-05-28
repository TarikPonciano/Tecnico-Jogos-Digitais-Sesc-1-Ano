class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def aumentarSalario(self, percentual):
        self.salario = self.salario * (100+percentual)/100
    def mostrarInformacoes(self):
        print(f'''
----- Informações do Funcionário ------
Nome: {self.nome}
Salário: R$ {self.salario:.2f}
''')