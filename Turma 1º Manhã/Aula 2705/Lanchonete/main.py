from classLanche import Lanche
# Implemente no Lanche um método chamado "mostrarInformacoes", que deverá exibir as informações do lanche no formato: "{nome} - R$ {preco:.2f} - {tipo}"
cardapio = {
    1: Lanche("Dogão", 15, "Comida"),
    2: Lanche("Beirute", 15, "Comida"),
    3: Lanche("Mistão", 7, "Comida"),
    4: Lanche("Hamburgão", 20, "Comida"),
    5: Lanche("Coca-Zero", 5, "Bebida"),
    6: Lanche("Milk-shake", 13, "Bebida")
}

cardapio[6].setTipo("Comida")
cardapio[6].setPreco(30)
print(cardapio[6].getPreco())
# Exiba o cardápio formatado para o usuário
print(f'''
1.  {cardapio[1].mostrarInformacoes()}
2.  {cardapio[2].mostrarInformacoes()}
3.  {cardapio[3].mostrarInformacoes()}
4.  {cardapio[4].mostrarInformacoes()}
5.  {cardapio[5].mostrarInformacoes()}
6.  {cardapio[6].mostrarInformacoes()}
''')

# print("AUTOMATIZADO")
# for chave in cardapio.keys():
#     print(f"{chave}. {cardapio[chave].mostrarInformacoes()}")

# for i in range(1,len(cardapio)+1):
#     print(cardapio[i].mostrarInformacoes())