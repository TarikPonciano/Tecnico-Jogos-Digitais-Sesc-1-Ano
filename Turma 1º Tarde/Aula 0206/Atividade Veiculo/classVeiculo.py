class Veiculo:
    def __init__(self, marca, modelo, quilometragem):
        self.marca = marca
        self.modelo = modelo
        if (quilometragem < 0):
            self.quilometragem = 0
        else:
            self.quilometragem = quilometragem
    def rodar(self, distancia):
        self.quilometragem += distancia

        print(f"O veículo {self.marca} {self.modelo} já rodou no total: {self.quilometragem}km!")