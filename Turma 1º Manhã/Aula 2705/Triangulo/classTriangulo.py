class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    def calcularPerimetro(self):
        return self.ladoA + self.ladoB + self.ladoC
    def calcularArea(self):
        return ((self.ladoA * self.ladoB * self.ladoC)/self.getMaiorLado())/2
    def getMaiorLado(self):

        maior = self.ladoA

        if self.ladoB >= maior:
            maior = self.ladoB
        elif self.ladoC >= maior:
            maior = self.ladoC
        
        return maior