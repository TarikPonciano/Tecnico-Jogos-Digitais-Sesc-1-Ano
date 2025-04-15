def somar(a, b):
    soma = a + b
    print("A soma é: ", soma)

def subtrair(a, b):
    subtracao = a - b
    print("A subtração é: ", subtracao)

def multiplicar(a, b):
    multiplicacao = a * b
    print("A multiplicação é :", multiplicacao)

def dividir(a, b):
    divisao = a / b
    print("A divisão é :", divisao)

def receber_entrada_1():
    valor1 = float(input("Insira o valor 1: "))
    return valor1

def receber_entrada_2():
    valor2 = float(input("Insira o valor 2: "))
    return valor2

def main():
    escolha = int(input("Insira sua escolha - 1 a 4: "))
    a = receber_entrada_1()
    b = receber_entrada_2()

    if(escolha == 1):
        somar(a, b)
    elif(escolha == 2):
        subtrair(a, b)
    elif(escolha == 3):
        multiplicar(a, b)
    elif(escolha == 4):
        dividir(a, b)
    else:
        print("Opção inválida")

main()
