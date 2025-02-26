import random

bilhete = ""
numeroPremiado = str(random.randint(10,60))

for i in range(6):
    numeroDaSorte = str(random.randint(10,60))

    if numeroDaSorte in bilhete:
        numeroDaSorte = str(random.randint(10,60))
        
    else:
        bilhete += " " + numeroDaSorte

print("Seu bilhete da sorte:", bilhete)

if (numeroPremiado in bilhete):
    print("Parabéns você ganhou!")
else:
    print("Que pena você perdeu!")

print("O número da sorte é:",numeroPremiado)
