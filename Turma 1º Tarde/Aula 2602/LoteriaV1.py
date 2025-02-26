bilhete = ""

numeroPremiado = "6"

for i in range(6):

    numeroDaSorte = input(f"Escreva um numero de 01 a 60:")

    if (i == 0):
        bilhete += numeroDaSorte
    else:
        bilhete += " - " + numeroDaSorte

print(f"Bilhete da Sorte: {bilhete}")

if (numeroPremiado in bilhete):
    print("EBAAAAAAA. Parabéns você venceu! :)")
else:
    print("AAaaaaaahhhh. Que pena, você perdeu! :(")



