numero = int(input("Digite um número: "))

qtdDivisores = 0
divisores = "" 
for i in range(2, (numero+1)):
    if (numero % i == 0 ):
        qtdDivisores += 1
        divisores += str(i) + " "

if (qtdDivisores <= 1):
    print(f"O número {numero} é primo!")
    
else:
    print(f"O número {numero} não é primo!")

print(f"Os divisores desse número são: {divisores}")