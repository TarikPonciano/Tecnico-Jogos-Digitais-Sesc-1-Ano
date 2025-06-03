from classesPersonagens import Jogador, Inimigo


jogador = Jogador(100, 10, 5, 0)
inimigo1 = Inimigo(20, 5, 2, 5)

jogador.mover("Sul")
jogador.ataqueEspecial(inimigo1)
inimigo1.atacar(jogador)
inimigo1.fugir()
jogador.atacar(inimigo1)