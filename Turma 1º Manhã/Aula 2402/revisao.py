# resultado = 1
# print("Calculadora de fatorial:")

# fatorial = int(input("Digite o fatorial desejado:"))

# for i in range(1,fatorial+1):
#     resultado *= i

# print(f"{fatorial}! = {resultado}")


# for i in range(1,100,10):
#     print(i)

# nomes = ""

# for i in range(5):
#     novoNome = input("Digite um novo nome: ")
#     nomes += " " + novoNome

# print(nomes)


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

# boletim = []
# soma = 0

# for i in range(4):
#     nota = float(input("Digite sua nota: "))
    
#     boletim.append(nota)
    
#     soma += nota

# print("Boletim:", boletim[0])
# print("Média:",(soma/4))

