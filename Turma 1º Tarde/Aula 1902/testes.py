# Crie um programa que pede seu nome e imprime "Olá {nome}!" 5 vezes.
'''
nome = input("Digite seu nome:")

for i in range(5):
    print(f"Olá, {nome}!")
'''

# Crie um programa que repete 5 vezes as seguintes instruções:
# Pede o nome do usuário
# Imprime "Olá, {nome}!"

'''
for i in range(5):
    nome = input("Digite o nome:")
    print(f"Olá, {nome}!")
'''
# Crie um programa que use loop for para calcular a soma de 1 até 1000
'''
soma = 0

for i in range(1,1001):
    print(f"Processo de soma: {soma+i} = {soma} + {i}")
    soma = soma + i

print("Soma:",soma)
'''
# Crie um programa que use loop for para calcular a média da soma de 1 até 1000
'''
soma = 0
qtdNumeros = 0

for i in range(1,1001):
    soma += i
    qtdNumeros += 1

media = soma / qtdNumeros

print("A média de 1 até 1000 é:",media)
'''


# Crie um programa que exibe apenas os números pares de 1 até 1000
qtd = 0
soma = 0
for i in range(1, 1001):
    if (i % 2 == 0):
        print(i)
        qtd += 1
        soma += i

print("Quantidade de numeros pares:", qtd)
print("Soma dos numeros pares:", soma)

