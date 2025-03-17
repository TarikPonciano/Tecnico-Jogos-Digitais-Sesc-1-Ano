notas = []

for i in range(10):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

contador = 1
for nota in notas:
    print(f"Bimestre {contador}: {nota}")
    contador += 1
