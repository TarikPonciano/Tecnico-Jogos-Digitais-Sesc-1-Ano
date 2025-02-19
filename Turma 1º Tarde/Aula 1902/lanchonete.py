print("Bem vindo a Para Lanches")

qtd = int(input("Digite quantos produtos deseja pedir:"))

nomes = ""
valorTotal = 0

for i in range(qtd):
    print('''
Cardapio:
          
01 - Cachorro Quente - 5
02 - Coxinha - 10
03 - Mousse de Chocolate - 7.5
          
00 - Sair

''')
    codigo = input("Digite o codigo do produto:")

    if(codigo == "00"):
        print("Encerrando as compras...")
        break

    if (codigo == "01"):
        nome = "Cachorro Quente"
        preco = 5
    elif (codigo == "02"):
        nome = "Coxinha"
        preco = 10
    elif (codigo == "03"):
        nome = "Mousse de Chocolate"
        preco = 7.5
    else:
        nome = "Produto Inválido"
        preco = 0

    nomes += nome + "\n"
    valorTotal += preco

print(f'''
Produtos:
      {nomes}

Valor total: R$ {valorTotal}

''')
