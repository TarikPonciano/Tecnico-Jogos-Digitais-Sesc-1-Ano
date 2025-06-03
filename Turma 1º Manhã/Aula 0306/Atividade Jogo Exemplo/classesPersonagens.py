class Personagem():
    def __init__(self, vida, dano, velocidade, posicao):
        self.vida = vida
        self.dano = dano
        self.velocidade = velocidade
        self.posicao = posicao
    def tomarDano(self, dano):
        self.vida -= dano
        print(f"O personagem tomou dano e agora está com {self.vida} de vida!")
    def mover(self):
        self.posicao += self.velocidade
        print(f"O personagem se moveu e agora está na posição {self.posicao}")
    def atacar(self, inimigo):
        if (self.posicao == inimigo.posicao):
            print(f"O personagem atacou causando {self.dano} de dano!")
            inimigo.tomarDano(self.dano)
           
        else:
            print("Você deve estar na mesma posição do inimigo!")

class Jogador(Personagem):
    def __init__(self, vida, dano, velocidade, posicao):
        super().__init__(vida, dano, velocidade, posicao)
    def ataqueEspecial(self, inimigo):
        if (self.posicao == inimigo.posicao):
            print(f"O personagem atacou causando {self.dano*2} de dano!")
            inimigo.tomarDano(self.dano*2)
           
        else:
            print("Você deve estar na mesma posição do inimigo!")

    def tomarDano(self, dano):
        super().tomarDano(dano/2)
    def mover(self, direcao):
        if (direcao == "Norte"):
            self.posicao += self.velocidade
        elif (direcao == "Sul"):
            self.posicao -= self.velocidade


class Inimigo(Personagem):
    def __init__(self, vida, dano, velocidade, posicao):
        super().__init__(vida, dano, velocidade, posicao)
    def fugir(self):
        self.posicao -= self.velocidade
        print(f"O personagem se moveu e agora está na posição {self.posicao}")
