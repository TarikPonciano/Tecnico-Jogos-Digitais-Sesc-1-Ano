#Crie um jogo que executa indefinidamente.
 
#A cada repetição desse jogo, peça para que o usuário escreva algo. Se o usuário escrever "Sair", o jogo deverá ser finalizado. Se o usuário escrever qualquer outra coisa, o jogo deverá ir para a próxima repetição.

#A cada repetição você deve imprimir o número de "pontos" na tela, e antes de cada repetição o valor dos pontos deve aumentar em 1.

#Crie uma opção chamada "Upgrade", que faz o usuário gastar seus pontos mas aumenta o seu ganho em 1 para cada vez que foi comprado.

pontos = 0

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
    else:
        print("Você ganhou 1 ponto!")
        pontos += 1