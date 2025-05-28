class Funcionario:
    def __init__(self, nome, cpf, salario, idade):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.idade = idade

    def getNome(self):
        return self.nome
    def setNome(self, novoNome):
        self.nome = novoNome

    def getSalario(self):
        return self.salario
    def setSalario(self, novoSalario):
        if novoSalario >= 1518:
            self.salario = novoSalario
        elif novoSalario < 0:
            
            print("Tentativa de cadastro de salário inválido!")
        else: 
            self.salario = 1518
    
    def getCpf(self,senha):
        if senha == "123456":
            return self.cpf
        else:
            print("INFORMAÇÃO RESTRITA")
    
    def mostrarInformacoes(self):
        print(f'''
----- Informações Pessoais -----
    Nome: {self.nome}
    CPF: {self.cpf}
    Salário: R$ {self.salario:.2f}
    Idade: {self.idade} anos
''')