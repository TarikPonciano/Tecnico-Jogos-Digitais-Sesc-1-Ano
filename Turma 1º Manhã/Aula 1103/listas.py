notas = []

for i in range(4):
    nota = float(input("Digite uma nota: "))

    notas.append(nota)

contador = 1
for n in notas:
    print(f"Bimestre {contador} - {n}")
    contador += 1


print(notas[4])