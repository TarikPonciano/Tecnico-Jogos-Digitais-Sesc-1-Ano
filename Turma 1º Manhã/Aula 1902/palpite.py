#Crie um programa que possui um número secreto definido por você. Permita que o usuário dê um palpite, se o palpite for correto, ou seja, palpite == numeroSecreto, você deverá imprimir 'Vitória'. Se o palpite for incorreto você deverá imprimir 'Derrota'.

#Ao errar indique se o número é maior ou menor que o palpite.

#Utilizando o loop for, permita que a pessoa tenha 3 tentativas

#Se a pessoa acertar, termine o loop mais cedo
import random
numeroAluno = random.randint(1,38)
print(f"O aluno sorteado foi o {numeroAluno}")
numeroSecreto = random.randint(1,100)


print("Jogo da Advinhação")
tentativas = 0

for i in range(3):
    palpite = int(input("Digite um número de 1 a 100:"))
    tentativas += 1

    if (palpite == numeroSecreto):
        print("Você venceu!")
        break
    else:
        print("Você perdeu!")
        if (tentativas == 3):
            print("Você chegou ao limite de tentativas!")
            break

        if (palpite > numeroSecreto):
            print("Chute mais baixo!")
        else:
            print("Chute mais alto!")



print("FIM DE JOGO!")

print("O número era:",numeroSecreto)
