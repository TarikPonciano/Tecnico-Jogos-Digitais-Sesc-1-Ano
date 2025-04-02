lista = ["Maçã", "Acerola", "Cereja", "Banana", "Banana", "Banana"]

print(lista[1])

lista[1] = "Abacate"

print(lista[1])

lista.append("Maracujá")
lista.insert(0, "Romã")

print(lista)

lista.pop(1)
lista.remove("Romã")

print(lista)

print(lista.count("Banana"))
print(len(lista))
print(lista.index("Maracujá"))
