total = 0
produtos = ""

qtdProdutos = int(input("Digite quantos produtos deseja comprar:"))

for i in range (qtdProdutos):
    
    produto = input("Digite o nome do produto:")
    if produto == "Sair":
        break
    preco = float(input("Digite o preco do produto:"))

    total = total + preco
    produtos = produtos + produto + "\n"


print(f"Você comprou: {produtos}")
print(f"Você gastou: R$ {total}")    