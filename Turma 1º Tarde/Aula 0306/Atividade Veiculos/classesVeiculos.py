class Veiculo:
    def __init__(self, marca, modelo, cor, velocidade, tipo):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = velocidade
        self.tipo = tipo

    def acelerar(self):
        self.velocidade += 5
        print(f"O veículo {self.marca} {self.modelo} acelerou para {self.velocidade} km/h")

    def desacelerar(self):
        self.velocidade -= 5
        print(f"O veículo {self.marca} {self.modelo} desacelerou para {self.velocidade} km/h")

    def parar(self):
        self.velocidade += 0
        print(f"O veículo {self.marca} {self.modelo} parou completamente")

    def mostrarInformacoes(self):
        print(f'''

----- Informações Veículos -----
Marca: {self.marca}
Modelo: {self.modelo}
Cor: {self.cor}
Tipo: {self.tipo}
Velocidade: {self.velocidade} km/h
''')
        
class Trem(Veiculo):
    def __init__(self, marca, modelo, cor, velocidade):
        super().__init__(marca, modelo, cor, velocidade, "Terrestre")
    def buzina(self):
        print("BEEEEEEEEEEEEM BEEEEEMMMM")

