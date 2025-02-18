#Criar um programa que pede o nome do lanche a ser comprado, a quantidade do lanche a ser comprado e o preço do lanche a ser comprado. Calcule o valor total do pedido e exiba ao final "Obrigado por comprar na XYZ Lanches. O valor do seu pedido foi R$ {total} e você comprou {quatidade} {nomeDoProduto}"
nomeLanche = input("Digite o nome do lanche: ")
quantidadeLanche = int(input("Digite quantas unidades você deseja: "))
precoLanche = float(input("Digite o preço: R$"))

valorTotal = quantidadeLanche * precoLanche

print(f"Obrigado por comprar na XYZ Lanches. O total do seu pedido foi R$ {valorTotal}. Você comprou {quantidadeLanche} unidades de {nomeLanche}")
