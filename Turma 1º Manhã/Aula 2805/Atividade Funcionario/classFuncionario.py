class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome

        if salario >= 1518:
            self.salario = salario
        else:
            self.salario = 1518

    def aumentarSalario(self, aumento):
        novoSalario =  self.salario * (100+aumento)/100 
        print(f"Aumento salarial de {aumento}%. O colaborador {self.nome} ganhava R$ {self.salario:.2f} e agora ganhará R$ {novoSalario:.2f}!")

        self.salario = novoSalario