print("Bem vindo a lanchonete!")

print("Escolha até 5 produtos!")
total = 0
produtos = ""

for i in range(3):
    produto = input("Digite o nome do produto:")
    preco = float(input("Digite o preço do produto:"))
    total += preco
    produtos += produto + "\n"

print("O total da sua compra foi: ",total)
print("Produtos comprados: ",produtos)


