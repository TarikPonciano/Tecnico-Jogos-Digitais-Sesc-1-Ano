# limiteInferior = int(input("Digite o número inicial: "))
# limiteSuperior = int(input("Digite o número final: "))

# if limiteInferior>limiteSuperior:
#     backup = limiteInferior
#     limiteInferior = limiteSuperior
#     limiteSuperior = backup

# soma = 0
# for i in range(limiteInferior,limiteSuperior+1):
#     soma += i

# print(f"Somatório de {limiteInferior} até {limiteSuperior} = {soma}")

numero = 1
soma = 0

while (numero <= 100):
    soma += numero
    numero += 1

print(soma)