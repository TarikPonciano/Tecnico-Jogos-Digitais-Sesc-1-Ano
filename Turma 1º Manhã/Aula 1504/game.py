#Crie um jogo que executa indefinidamente.
 
#A cada repetição desse jogo, peça para que o usuário escreva algo. Se o usuário escrever "Sair", o jogo deverá ser finalizado. Se o usuário escrever qualquer outra coisa, o jogo deverá ir para a próxima repetição.

#A cada repetição você deve imprimir o número de "pontos" na tela, e antes de cada repetição o valor dos pontos deve aumentar em 1.

#Crie uma opção chamada "Upgrade", que faz o usuário gastar seus pontos mas aumenta o seu ganho em 1 para cada vez que foi comprado.

pontos = 0
poderClick = 1
upgrades = {
    "1": {"nome":"Mouse Quebrado", "efeito": 1, "custo": 100, "quantidade": 0},
    "2": {"nome":"Irmão Mais Novo", "efeito": 5, "custo": 1000, "quantidade": 0},
    "3": {"nome":"Bot de click", "efeito":20, "custo": 10000, "quantidade": 0}
}


while True:

    print(f'''
          
-------//---------
VOCÊ POSSUI: {pontos} PONTOS
-------//---------

''')

    resposta = input("Digite um dos comandos disponíveis:").lower()

    if (resposta == "sair"):
        print("Encerrando o jogo...")
        break
    elif (resposta == "loja"):
        print("Bem vindo à 'Loja de Upgrades'")
        
    else:
        print()
        print(f"Você ganhou {poderClick} ponto!")
        print()
        pontos += poderClick