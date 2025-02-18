# Crie um programa que exibe na tela todos os números de 0 até 100
for i in range(101):
    print(f"{i}. BAZINGA")

# Crie um programa que exibe na tela a soma de todos os números de 0 até 100
somatorio = 0
for i in range(101):
    print(f"-------- REPETIÇÃO {i+1} --------")
    print(f"Soma Atual: {somatorio}")
    print(f"Nova Soma: {somatorio} + {i} = {somatorio+i}")
    somatorio = somatorio + i
    print()
print("Resultado da Soma:",somatorio)
# Crie um programa que exibe na tela a média do somatório de todos os números de 0 até 100
somatorio = 0
quantidade = 0
for i in range(101):
    somatorio += i
    quantidade += 1

media = somatorio/quantidade
print("Resultado da Média:",media)

# Crie um programa que exibe na tela apenas números pares de 0 a 100

for i in range(101):
    if (i % 2 == 0):
        print(i)