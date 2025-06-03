class Pokemon:
    def __init__(self, nome, tipo, level):
        self.nome = nome
        self.tipo = tipo
        self.level = level
    
    def mostrarInformacoes(self):
        print(f'''
Nome: {self.nome}
Tipo: {self.tipo}
Level: {self.level}
''')