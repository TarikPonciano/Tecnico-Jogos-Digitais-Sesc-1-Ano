print("Bem vindo a lanchonete Para Lanches!")

print('''

Cardapio:
      
        100 - Cachorro Quente - R$ 1,10
        101 - Bauru Simples - R$ 1,30
      ''')

codigo = input("Digite o codigo do produto desejado: ")

if (codigo == "100"):
    nome = "Cachorro Quente"
    preco = 1.1
elif (codigo == "101"):
    nome = "Bauru Simples"
    preco = 1.3
elif (codigo == "102"):
    nome = "Bauru c/ovo"
    preco = 1.5
else:
    nome = "Codigo Invalido"
    preco = 0

quantidade = int(input("Digite quantas unidades deseja:"))
total = quantidade * preco

print(f"Voce comprou {nome}! Foram {quantidade} unidades! Voce gastou no total R$ {total:.2f}")