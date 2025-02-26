numero = int(input("Digite o número que deseja saber a tabuada: "))
multiplicacoes = int(input("Digite quantas multiplicações você quer na tabuada: "))

print(f"Tabuada do {numero} Com For")

for i in range(1, multiplicacoes+1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


print(f"Tabuada do {numero} Com While")

multiplicador = 1

while multiplicador <= multiplicacoes:
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
    multiplicador += 1