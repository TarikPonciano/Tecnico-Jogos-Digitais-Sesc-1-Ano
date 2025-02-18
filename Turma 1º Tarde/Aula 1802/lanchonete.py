print("BEM VINDO AO SISTEMA ALIMENTAR PARÁ LANCHES")

print()

print('''
        Cardápio:

        COD | Nome Lanche | Preço R$      

        100 | Cachorro Quente | R$ 1,10
        101 | Baurú Simples   | R$ 1,30
        102 | Baurú C/Ovo     | R$ 1,50
        103 | Hamburguer      | R$ 1,10
        104 | Cheeseburguer   | R$ 1,30
        105 | Refrigerante    | R$ 1,00
''')

codigo = input("Digite o codigo do produto:")

if (codigo == "100"):
    produto = "Cachorro Quente"
    preco = 1.10
elif (codigo == "101"):
    produto = "Baurú Simples"
    preco = 1.30
elif (codigo == "102"):
    produto = "Bauru C/Ovo"
    preco = 1.50
elif (codigo == "103"):
    produto = "Hamburguer"
    preco = 1.10
elif (codigo == "104"):
    produto = "Cheeseburguer"
    preco = 1.30
elif (codigo == "105"):
    produto = "Refrigerante"
    preco = 1.00
else:
    produto = "Produto Inválido"
    preco = 0

print(f"O produto escolhido foi {produto}!")

if (produto == "Produto Inválido"):
    print("Da próxima vez escolha um produto válido!")
else:
    quantidade = int(input("Digite a quantidade desejada: "))
    total = preco * quantidade
    print(f"Você comprou {quantidade} unidades de {produto} e pagou R$ {total:.2f}!")
