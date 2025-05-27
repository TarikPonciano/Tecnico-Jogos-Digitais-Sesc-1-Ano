class Pessoa:
    def __init__(self, nome, genero, cpf, ativo):
        self.nome = nome
        self.genero = genero
        self.cpf = cpf
        self.ativo = ativo
    def desativar(self):
        if (self.ativo == False): 
            print(f"{self.nome} não pode ser desativado novamente!")
        else:
            self.ativo = False
            print(f"{self.nome} foi desativado com sucesso!")

p1 = Pessoa("Nathan", "Masculino", "12345678910", True)
p2 = Pessoa("Caio", "Masculino", "93427947832", True)
p1.desativar()
p2.desativar()

