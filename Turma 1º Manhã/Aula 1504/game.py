#Crie um jogo que executa indefinidamente.
 
#A cada repetição desse jogo, peça para que o usuário escreva algo. Se o usuário escrever "Sair", o jogo deverá ser finalizado. Se o usuário escrever qualquer outra coisa, o jogo deverá ir para a próxima repetição.

#A cada repetição você deve imprimir o número de "pontos" na tela, e antes de cada repetição o valor dos pontos deve aumentar em 1.

#Crie uma opção chamada "Upgrade", que faz o usuário gastar seus pontos mas aumenta o seu ganho em 1 para cada vez que foi comprado.

#Implemente as melhorias realizadas no jogo

#Mude as informações do jogo para se encaixar em uma temática a sua escolha. 

#Crie 2 novos upgrades para o jogo

#Implemente pelo menos 1 nova mecânica

pontos = 0
poderClick = 1


upgrades = {
    "1": {"nome":"Mouse Quebrado", "efeito": 1, "custo": 100, "quantidade": 0, "descrição": "Mouse velho doado pela sua avó. Ele permite que você clique 1 vez a mais por repetição."},

    "2": {"nome":"Irmão Mais Novo", "efeito": 5, "custo": 1000, "quantidade": 0, "descrição": "Suborne seu irmão para que ele te ajude a clicar. Ele permite que você clique 5 vezes a mais por repetição."},
    
    "3": {"nome":"Bot de click", "efeito":20, "custo": 10000, "quantidade": 0, "descrição": "Utilizando os conhecimentos do curso técnico de jogos você cria um bot de click. Ele permite que você clique 20 vezes a mais por repetição."}
}


while True:

    print(f'''
          
-------//---------
VOCÊ POSSUI: \033[34m{pontos} PONTOS\033[0m
-------//---------

''')

    resposta = input("Digite um dos comandos disponíveis:").lower()

    if (resposta == "sair"):
        print("Encerrando o jogo...")
        break
    elif (resposta == "loja"):
        print()
        print("Bem vindo à 'Loja de Upgrades'")
        print()

        print("Upgrades:")

        for chave, informacoes in upgrades.items():
            print(f"{chave}. {informacoes["nome"]} - {informacoes["descrição"]} - {informacoes["efeito"]} cliques - Custo: {informacoes["custo"]} pontos")
            print()
        
        opcao = input("Digite o upgrade que deseja comprar: ")

        if opcao in upgrades:
            
            print(f"Você escolheu {upgrades[opcao]["nome"]}")
            print(f"Este upgrade custa {upgrades[opcao]["custo"]} pontos!")

            confirmacao = input("Você tem certeza que deseja comprar? S/N")

            if (confirmacao == "S"):

                if (pontos >= upgrades[opcao]["custo"]):
                    print(f"Você gastou {upgrades[opcao]["custo"]} pontos!")
                    pontos -= upgrades[opcao]["custo"]

                    print(f"Você ainda possui {pontos} pontos!")

                    print(f"Você adquiriu mais {upgrades[opcao]["efeito"]} poder de clique!")
                    poderClick += upgrades[opcao]["efeito"]
                    print(f"Seu poder de click agora é {poderClick}")
                    
                    upgrades[opcao]["quantidade"] += 1
                    print(f"Você possui um total de {upgrades[opcao]["quantidade"]} {upgrades[opcao]["nome"]}")

                else:
                    print("Dê o fora! Você não tem pontos suficientes para isso!")

            else:
                print("Até em breve forasteiro...")


        else:
            print("Escolha um upgrade válido da próxima vez!")
            

    else:
        print()
        print(f"Você ganhou {poderClick} ponto!")
        print()
        pontos += poderClick