def hello():
    print("Hello World")

def hello2(nome):
    print(f"Olá, {nome}!")

def saudacao(nome, idade, altura):
    print(f'''
    Olá, meu nome é {nome}!
    Tenho {idade} anos!
    Tenho {altura}m de altura!
''')

def soma(n1, n2):
    return n1 + n2


def dividir(n1,n2):
    if (n2==0):
        print("Divisão por 0!")
        return 0
    else:
        return n1/n2


saudacao("José", 25, 1.8)

