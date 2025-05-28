class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

        if (self.ladoA == self.ladoB and self.ladoB == self.ladoC):
            self.tipo = "Equilátero"
        elif(self.ladoA == self.ladoB or self.ladoB == self.ladoC or self.ladoA == self.ladoC):
            self.tipo = "Escaleno"
        elif (max(self.ladoA, self.ladoB, self.ladoC)*max(self.ladoA, self.ladoB, self.ladoC) == (self.ladoA*self.ladoA) + (self.ladoB + self.ladoB) + (self.ladoC + self.ladoC) - max(self.ladoA, self.ladoB, self.ladoC)*max(self.ladoA, self.ladoB, self.ladoC)):
            self.tipo = "Retangulo"

    def calcularPerimetro(self):
        perimetro = self.ladoA + self.ladoB + self.ladoC
        return perimetro
    def calcularArea(self):
        area = ((self.ladoA * self.ladoB * self.ladoC)/self.getMaiorLado()) / 2
        return area
    def getMaiorLado(self):
        maiorLado = max(self.ladoA, self.ladoB, self.ladoC)
        return maiorLado

