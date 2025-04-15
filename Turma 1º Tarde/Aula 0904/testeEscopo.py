def main():
    print("Bem vindo ao meu programa")

    print("No meu programa temos as funcionalidades: Elevar ao Quadrado, Inverter Numero")

    numero = int(input("Digite um numero para usar no meu programa: "))

    print("Numero ao quadrado: ", e(numero))
    print("Numero invertido: ", reverso(numero))

def e(b):
    a = b * b
    
    return a

def reverso (num):
    num = str(num)
    return num[::-1]

def f3(a):
    global x
    x = x + 1
    print(a+x)

x = 4
f3(3)
print(x)
