# soma = 0

# for i in range(1,1000001):
#     soma += i
    
# print(soma)


# numero = int(input("Digite o fatorial que deseja calcular:"))
# fatorial = 1

# fatorialTexto = ""

# for i in range(1,numero+1):
#     fatorial *= i

#     if (i == 1):
#         fatorialTexto += f"{i} "
#     else:
#         fatorialTexto += f"* {i} "


#     print(f"{fatorialTexto} = {fatorial}") 

# print(fatorial)

soma = 0
qtdNotas = 0
boletim = ""


for i in range(4):
    nota = float(input("Digite uma nota:" ))
    soma += nota
    qtdNotas += 1
    if (i == 0):
        boletim += f"Bimestre {i+1}: {nota}" 
    else:
        boletim += "\n" + f"Bimestre {i+1}: {nota}" 
    

print(f"Sua média é {soma/qtdNotas}")

print(boletim)


# Crie um programa que gera um bilhete de loteria com 6 números. Esse bilhete pode ser gerado de forma aleatória ou através de entradas do usuário.

# Verifique se algum dos números do bilhete é um número da sorte definido por você