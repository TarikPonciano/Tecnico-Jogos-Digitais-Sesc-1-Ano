#Faça um programa que usando for, exibe na tela a tabuada de um número:
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15
#.
#.
#.
#5 x 10 = 50
numero = int(input("Digite um número: "))

for i in range(1,11):
    #Fazer sua operação aqui
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
