print("SEJA BEM VINDO À LANCHONETE PARÁ LANCHES")
print()
print("Escolha um item do nosso cardápio:")

print('''
Código | Nome | R$ Preço
100 - Cachorro Quente - R$ 1,10
101 - Bauru Simples - R$ 1,30
102 - Bauru c/ovo - R$ 1,50
103 - Hamburguer - R$ 1,10
104 - Cheeseburguer - R$ 1,30
105 - Refrigerante - R$ 1,00

''')

codigo = input("Digite o código do produto desejado: ")

if (codigo == "100"):
    nome = "Cachorro Quente"
    preco = 1.10
elif (codigo == "101"):
    nome = "Bauru Simples"
    preco = 1.30
elif (codigo == "102"):
    nome = "Bauru c/ovo"
    preco = 1.50
else:
    nome = "Código Inválido"
    preco = 0
    print("VOCÊ DIGITOU UM CÓDIGO INVÁLIDO! PROGRAMA ABORTADO")
    exit()

quantidade = int(input("Digite quantas unidades você deseja:"))
total = preco * quantidade


print(f"Você comprou {nome}, consumindo {quantidade} unidades e pagou um total de R$ {total:.2f}")
