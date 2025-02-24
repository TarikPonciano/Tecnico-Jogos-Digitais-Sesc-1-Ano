# Crie um programa que gera um bilhete de loteria com 6 números. Esse bilhete pode ser gerado de forma aleatória ou através de entradas do usuário.

print("Bem vindo a Loteria dos Sonhos")
bilhete = ""
numeroSecreto = "10"

print("Escolha seus 6 números da sorte!")
print()
for i in range(6):
    numeroDaSorte = input("Digite um número de 1 a 60: ")
    bilhete += " " + numeroDaSorte

print(f"Seu Bilhete: {bilhete}")

if (numeroSecreto in bilhete):
    print("Você acertou!")
    print("O número sorteado é:",numeroSecreto)
else:
    print("Você errou!")