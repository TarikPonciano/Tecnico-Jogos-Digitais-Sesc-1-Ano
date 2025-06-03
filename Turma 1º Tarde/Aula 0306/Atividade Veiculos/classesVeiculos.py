class Veiculo:
    def __init__(self, modelo, cor, marca, tipo, velocidade):
        self.modelo = modelo
        self.cor = cor
        self.marca = marca
        self.tipo = tipo
        self.velocidade = velocidade
    def acelerar(self):
        self.velocidade += 5
        print(f"{self.modelo} {self.marca} {self.cor} acelerou e está há {self.velocidade} km/h")
    def desacelerar(self):

        self.velocidade -= 5
        
        if self.velocidade < 0:
            print("Não é possível desacelerar mais. O veículo está parado!")
            self.velocidade = 0
        else:
            print(f"{self.modelo} {self.marca} {self.cor} desacelerou e está há {self.velocidade} km/h")
    def parar(self):
        self.velocidade = 0
        print(f"{self.modelo} {self.marca} {self.cor} parou completamente!")

    def mostrarInformacoes(self):

        print(f'''
----- Informações do Veículo -----
Modelo: {self.modelo}
Marca: {self.marca}
Cor: {self.cor}
Tipo: {self.tipo}
Velocidade: {self.velocidade} km/h
''')