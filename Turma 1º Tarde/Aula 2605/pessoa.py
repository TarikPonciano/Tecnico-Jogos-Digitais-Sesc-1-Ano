class Pessoa:
    def __init__(self, nome, peso, idade, altura, estadoCivil):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.altura = altura 
        self.estadoCivil = estadoCivil

pessoa1 = Pessoa("Marquinhos", 70, 25, 1.75, "Solteiro")
pessoa2 = Pessoa("Joaquina", 50, 20, 1.55, "Casado")
print(f'''
----- Informações Pessoais -----
      
      Nome: {pessoa1.nome}
      Idade: {pessoa1.idade} anos
      Peso: {pessoa1.peso} Kg
      Altura: {pessoa1.altura}m 
''')

print(f'''
----- Informações Pessoais -----
      
      Nome: {pessoa2.nome}
      Idade: {pessoa2.idade} anos
      Peso: {pessoa2.peso} Kg
      Altura: {pessoa2.altura}m 
''')