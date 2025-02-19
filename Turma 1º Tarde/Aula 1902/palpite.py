#Crie um programa que possui um número secreto definido por você. Permita que o usuário dê um palpite, se o palpite for correto, ou seja, palpite == numeroSecreto, você deverá imprimir 'Vitória'. Se o palpite for incorreto você deverá imprimir 'Derrota'.

#Ao errar indique se o número é maior ou menor que o palpite.

#Utilizando o loop for, permita que a pessoa tenha 3 tentativas

#Se a pessoa acertar, termine o loop mais cedo    
import random 

alunoSorteado = random.randint(1,36)
numeroSecreto = random.randint(1,100)

print("Aluno Sorteado:", alunoSorteado)
tentativas = 0
for i in range(3):
    palpite = int(input("Digite um número de 1 a 100: "))
    tentativas += 1
    if (palpite == numeroSecreto):
        print("Você acertou!")
        break
    else:
        print("Você errou!")
        if (tentativas == 3):
            print("Fim das suas tentativas!")
            break
        if (palpite > numeroSecreto):
            print("Dê um chute menor!")
        else:
            print("Dê um chute maior!")

print("FIM DE JOGO")

print("O número era", numeroSecreto)