class Veiculo:
    def __init__(self, modelo, fabricante, identificador, velocidade, tipo):
        self.modelo = modelo
        self.fabricante = fabricante
        self.identificador = identificador
        self.velocidade = velocidade
        self.tipo = tipo

    def auto_destruir(self):
        print("O veículo explodiu em milhões de fragmentos!")

    def acelerar(self):
        self.velocidade += 5
        print(f"O veículo acelerou e agora está se movendo há {self.velocidade}km/h!")

    def desacelerar(self):

        self.velocidade -= 5

        if self.velocidade < 0:
            self.velocidade = 0
            print("O veículo já está parado, não é possível desacelerar ainda mais!")
        else:
            print(f"O veículo desacelerou e agora está se movendo há {self.velocidade}km/h!")

    def parar (self):
        self.velocidade = 0
        print("O veículo parou por completo!")

    def mostrarInformacoes(self):
        print(f'''
----- Informações do Veículo -----              

Modelo: {self.modelo}
Fabricante: {self.fabricante}
ID: {self.identificador}
Tipo: {self.tipo}
Velocidade Atual: {self.velocidade}km/h
''')

class Trem(Veiculo):
    def __init__(self, modelo, fabricante, identificador, velocidade):
        super().__init__(modelo, fabricante, identificador, velocidade, "Terrestre")

class Aviao(Veiculo):
    def __init__(self, modelo, fabricante, identificador, velocidade):
        super().__init__(modelo, fabricante, identificador, velocidade, "Aéreo")
    def decolar():
        print("O avião decolou!")

class Navio(Veiculo):
    def __init__(self, modelo, fabricante, identificador, velocidade):
        super().__init__(modelo, fabricante, identificador, velocidade, "Aquático")