print("Versão For")

# achados = 0
# achadosTexto = ""

# for i in range(10):
#     numero = int(input("Digite um número: "))

#     if (numero >= 10 and numero <= 50):
#         print("Achei um número no intervalo!")
#         achados += 1
#         achadosTexto += " " + str(numero)

# print("Números no intervalo:", achados)
# print("Números no intervalo:", achadosTexto)


print("Versão While")
achados = 0
achadosTexto = ""

while achados < 5:
    
    numero = int(input("Digite um número: "))

    if (numero >= 10 and numero <= 50):
        print("Achei um número no intervalo!")
        achados += 1
        achadosTexto += " " + str(numero)

print("Números no intervalo:", achados)
print("Números no intervalo:", achadosTexto)

