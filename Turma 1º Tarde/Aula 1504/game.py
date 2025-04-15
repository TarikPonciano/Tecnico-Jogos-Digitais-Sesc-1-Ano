# Crie um programa que repete indefinidamente.

# Dentro da repetição criar uma variável para pedir ao usuário o que ele deseja fazer. Se a resposta dele for 'sair', o programa deverá encerrar. Se for qualquer outra coisa, o programa deverá continuar.

# Dentro da repetição, antes de pedir que o usuário digite. Imprima na tela "SALDO DE PONTOS: {pontos} pontos". A cada repetição incrementar os pontos em 1.

# Crie um sistema de upgrade. Se a pessoa escrever a palavra "upgrade" você deverá oferecer um item que custa 100 pontos para ela. Para comprar o item, a pessoa deverá confirmar que quer comprar e deverá possuir PELO MENOS 100 pontos de saldo. Após comprar o item, cada 'clique' deverá valer 1 ponto a mais.

# Substitua a ação de 'upgrade' por uma 'loja'. Essa loja deverá exibir pelo menos 3 opções de upgrade. Cada upgrade deve ter um nome, uma descrição, um custo e um valor de efeito(poderClick). O jogador deverá escolher um dos itens da lista e confirmar a compra. Se o jogador não tiver pontos suficientes, você deverá imprimir uma mensagem de erro, se tiver deverá incrementar o seu poder de clique total.

# Crie uma variável no início do código chamado 'upgrades', dentro dessa variável crie cada um dos 3 upgrades e cadastre suas informações.

import os

pontos = 0
poderClick = 1

upgrades = {
    "1": {"nome": "Mouse Quebrado", "descrição": "Você compra um mouse quebrado na feira da parangaba. Agora você pode clicar com 1 mão a mais!", "efeito": 1, "custo": 100, "quantidade": 0},

    "2": {"nome": "Irmão Mais Novo", "descrição": "Encomenda um irmão mais novo na shopee para que ele clique por você!", "efeito": 5, "custo": 1000, "quantidade": 0 },

    "3": {"nome": "Script Python", "descrição": "Utilizando as técnicas aprendidas em um curso profissionalizante do Senac você cria um script para clicar por você!", "efeito": 50, "custo": 15000, "quantidade": 0 }
}



while True:
    
    print(f'''
          
--------------------------------          
SALDO DE PONTOS: {pontos} pontos
--------------------------------    
    
    ''')
    resposta = input("Digite o que deseja fazer: ").lower()
    os.system("cls")
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

    

