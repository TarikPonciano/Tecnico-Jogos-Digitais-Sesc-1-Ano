# # Mude o programa para que a pessoa possa especificar o inicio e o fim do somatório.
# print ("Calculador de somatório")
# inicio = int(input("Digite o numero inicial: "))
# fim = int(input("Digite o numero final: "))

# if (inicio > fim):
#     backup = inicio
#     inicio = fim
#     fim = backup

# soma = 0

# for i in range(inicio,fim+1):
#     soma += i

# print(f"Somatório de {inicio} até {fim} = {soma}")

# soma = 0

# contador = 1

# while(contador <= 100):
#     soma += contador
#     contador += 1

# print(soma)

# altura = int(input("Digite a altura do retângulo:"))
# largura = int(input("Digite a largura do retângulo:"))

# linha = ""

# for i in range(largura):
#     linha += "#"

# for i in range(altura):
#     print(linha)

numero = int(input("Digite o seu número: "))

divisores = 0
listaDivisores = []

for i in range(2, numero+1):
    if (numero % i == 0 ):
        divisores += 1
        listaDivisores.append(i)

if divisores <= 1:
    print(f"O número {numero} é primo!")
else:
    print(f"O número {numero} não é primo!")

print(f"Lista de Divisores: {listaDivisores}")