# Crie uma classe Lanche que contenha 3 informações sobre o lanche.

class Lanche:
    def __init__(self, nome, preco, tipo):
        self.nome = nome
        self.preco = preco
        self.tipo = tipo
    def mostrarInformacoes(self):
        return f"{self.nome} - R$ {self.preco:.2f} - {self.tipo}"
    
    def getNome(self):
        return self.nome
    
    def setNome(self, novoNome):
        self.nome = novoNome

    def getPreco(self):
        return f"R$ {self.preco:.2f}"
    
    def setPreco(self, novoPreco):
        if novoPreco >= 0:
            self.preco = novoPreco

    def getTipo(self):
        return self.tipo
    
    def setTipo(self, novoTipo):
        if novoTipo != "Comida" and novoTipo != "Bebida":
            print("ESCOLHA UM TIPO VÁLIDO PARA O LANCHE")
        else:
            self.tipo = novoTipo

        