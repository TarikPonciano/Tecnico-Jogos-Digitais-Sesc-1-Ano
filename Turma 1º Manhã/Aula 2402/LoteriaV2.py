# Crie um programa que gera um bilhete de loteria com 6 números. Esse bilhete pode ser gerado de forma aleatória ou através de entradas do usuário.
import random

print("Bem vindo à Loteria dos Sonhos!")
bilhete = ""
numeroSecreto = random.randint(1,60)

print("Escolha seus 6 números da sorte!")
print()

for i in range(6):
    numeroDaSorte = random.randint(1,60)

    if (str(numeroDaSorte) in bilhete):
        numeroDaSorte = random.randint(1,60)

    bilhete += " " + str(numeroDaSorte)

print("Bilhete:",bilhete)

if (str(numeroSecreto) in bilhete):
    print("Parabéns, seu bilhete contém o número secreto! :) ")
else:
    print("Que pena, seu bilhete não contém o número secreto! :( ")

print("O número secreto era:", numeroSecreto)