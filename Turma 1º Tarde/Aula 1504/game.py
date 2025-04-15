# Crie um programa que repete indefinidamente.

# Dentro da repetição criar uma variável para pedir ao usuário o que ele deseja fazer. Se a resposta dele for 'sair', o programa deverá encerrar. Se for qualquer outra coisa, o programa deverá continuar.

# Dentro da repetição, antes de pedir que o usuário digite. Imprima na tela "SALDO DE PONTOS: {pontos} pontos". A cada repetição incrementar os pontos em 1.

# Crie um sistema de upgrade. Se a pessoa escrever a palavra "upgrade" você deverá oferecer um item que custa 100 pontos para ela. Para comprar o item, a pessoa deverá confirmar que quer comprar e deverá possuir PELO MENOS 100 pontos de saldo. Após comprar o item, cada 'clique' deverá valer 1 ponto a mais.

# Substitua a ação de 'upgrade' por uma 'loja'. Essa loja deverá exibir pelo menos 3 opções de upgrade. Cada upgrade deve ter um nome, uma descrição, um custo e um valor de efeito(poderClick). O jogador deverá escolher um dos itens da lista e confirmar a compra. Se o jogador não tiver pontos suficientes, você deverá imprimir uma mensagem de erro, se tiver deverá incrementar o seu poder de clique total.

# Crie uma variável no início do código chamado 'upgrades', dentro dessa variável crie cada um dos 3 upgrades e cadastre suas informações.


pontos = 0
poderClick = 1

while True:
    
    print(f'''
          
--------------------------------          
SALDO DE PONTOS: {pontos} pontos
--------------------------------    
    
    ''')
    resposta = input("Digite o que deseja fazer: ").lower()
        
    if (resposta == "sair"):
        print("Encerrando o jogo...")
        break
    if (resposta == "upgrade"):
        print('''
    Nome: Luva de Gatinho
    Efeito: Seus cliques valem 1 ponto a mais!
    Custo: 100
''')
        confirmacao = input("Você deseja comprar esse item? (S/N)")

        if (confirmacao == "S"):
            if (pontos >= 100):
                poderClick += 1
                pontos -= 100
            else:
                print("Você não possui pontos o suficiente. CLIQUE MAIS!")
        else:
            print("Até logo forasteiro...")

    else:
        print()
        print(f"Você ganhou {poderClick} pontos!")
        print()
        pontos += poderClick 

