bilhete = ""

for i in range(6):

    numeroDaSorte = input(f"Escreva um numero de 1 a 60:")

    if (i == 0):
        bilhete += numeroDaSorte
    else:
        bilhete += " - " + numeroDaSorte

print(f"Bilhete da Sorte: {bilhete}")




