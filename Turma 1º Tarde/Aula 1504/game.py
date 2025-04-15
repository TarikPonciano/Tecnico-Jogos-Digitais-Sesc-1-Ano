# Crie um programa que repete indefinidamente.

# Dentro da repetição criar uma variável para pedir ao usuário o que ele deseja fazer. Se a resposta dele for 'sair', o programa deverá encerrar. Se for qualquer outra coisa, o programa deverá continuar.

# Dentro da repetição, antes de pedir que o usuário digite. Imprima na tela "SALDO DE PONTOS: {pontos} pontos". A cada repetição incrementar os pontos em 1.

pontos = 0

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
    else:
        print()
        print("Você ganhou 1 ponto!")
        print()
        pontos += 1

