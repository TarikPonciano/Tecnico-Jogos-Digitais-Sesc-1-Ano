class Pessoa:
    def __init__(self, nome, genero, cpf, ativo):
        self.nome = nome
        self.genero = genero
        self.cpf = cpf
        self.ativo = ativo

    def desativar(self):
        if (self.ativo == True):
            self.ativo = False
            print(f"O usuário {self.nome} foi desativada com sucesso!")
        else:
            print("Não é possível desativar o que já foi desativado!")
    
    def mostrarInformacoes(self):
        print(f'''
----- Informações Pessoais -----
    Nome: {self.nome}
    Gênero: {self.genero}
    CPF: {'*' * len(self.cpf)}
    Situação: {"Ativo" if self.ativo else "Inativo"}
''')