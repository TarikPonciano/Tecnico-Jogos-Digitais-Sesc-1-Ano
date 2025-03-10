largura = int(input("Digite a largura do retângulo desejado: "))

altura = int(input("Digite a altura do retângulo desejado: "))


####
#  #
#  #
####

linhaVazada = ""
linhaPreenchida = ""
for i in range(largura):
    linhaPreenchida += "#"

    if (i==0 or i==(largura-1)):
        linhaVazada += "#"
    else:
        linhaVazada += " "



for i in range(altura):
    if (i == 0 or i==(altura-1)):
        print(linhaPreenchida)
    else:
        print(linhaVazada)