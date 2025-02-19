# Crie um programa de lanchonete que pede ao usuario o nome do lanche, a quantidade e o preço do lanche. Calcule o valor total da compra e ao final exiba a mensagem "Obrigado pela preferencia. A Lanchonete Para Lanches lhe aguarda na proxima vez. \nO total da sua compra foi R$ {total} e voce comprou {quantidade} {nomeDoLanche}"

print("BEM VINDO AO PARA LANCHES")

nomeProduto = input("Digite o nome do produto desejado: ")

quantidadeProduto = int(input("Digite quantas unidades deseja: "))

precoProduto = float(input("Digite o preço do produto: R$"))

valorTotal = quantidadeProduto * precoProduto

print(f'''
Obrigado pela preferencia!
A Para Lanches agradece sua visita!
      
Sua compra deu um total de R$ {valorTotal:.2f}.
Voce comprou {quantidadeProduto} unidades de {nomeProduto}!

''')