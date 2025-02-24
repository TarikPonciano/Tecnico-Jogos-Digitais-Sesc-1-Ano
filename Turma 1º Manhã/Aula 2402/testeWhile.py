# print("O que é que cai em pé e corre deitado: ")

# resposta = input("Digite a resposta do enigma:")

# while(resposta != "chuva"):
#     resposta = input("Você errou! Tente novamente: ")

# print("Você acertou!")
#Crie um programa que pergunta um enigma a alguém. A pergunta deve ser repetida até que a pessoa acerte. Ou seja, enquanto a tentativa for diferente da resposta correta, repita.

resposta = ""
tentativas = 0
pontuacao = 0

while resposta != "homem" and tentativas < 3:
    resposta = input("O que é, o que é. De manhã tem 4 pernas, de tarde tem 2 e à noite tem 3: ")

    tentativas += 1

    if (resposta != "homem"):
        print("Você errou!")
        print("Tentativas restantes:", (3-tentativas))
    else:
        print("Você acertou!")
        pontuacao += 10 * (4-tentativas)

print("Sua pontuação final foi:", pontuacao)
print("Fim de Jogo!")
