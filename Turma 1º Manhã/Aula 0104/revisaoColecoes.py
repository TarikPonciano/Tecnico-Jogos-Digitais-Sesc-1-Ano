# listas = ["maçã","cereja","acerola"]

# print(listas[1])

# listas[1] = "maracujá"

# print(listas[1])

# print(listas)

# listas.append("cajá")
# listas.insert(0, "romã")

# print(listas)

# listas.pop(1)
# listas.remove("maracujá")

# print(listas)

# print(f"Sobraram {len(listas)} frutas ")

# print(listas.count("acerola"))
# print(listas.index("romã"))

produto = {"preço": 4.50, "nome": "Coxinha", "marca": "Fabricação Própria", "código": 1, "validade": "5 dias uteis" }

print(produto["nome"])


produto["nome"] = "Enroladinho"

print(produto)

produto["fabricação"] = "01/04/2025"

print(produto)
print(produto.keys())
print(produto.values())