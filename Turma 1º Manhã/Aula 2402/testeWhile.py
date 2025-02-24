# print("O que é que cai em pé e corre deitado: ")

# resposta = input("Digite a resposta do enigma:")

# while(resposta != "chuva"):
#     resposta = input("Você errou! Tente novamente: ")

# print("Você acertou!")
#Crie um programa que pergunta um enigma a alguém. A pergunta deve ser repetida até que a pessoa acerte. Ou seja, enquanto a tentativa for diferente da resposta correta, repita.

# resposta = ""
# tentativas = 0
# pontuacao = 0

# while resposta != "homem" and tentativas < 3:
#     resposta = input("O que é, o que é. De manhã tem 4 pernas, de tarde tem 2 e à noite tem 3: ")

#     tentativas += 1

#     if (resposta != "homem"):
#         print("Você errou!")
#         print("Tentativas restantes:", (3-tentativas))
#     else:
#         print("Você acertou!")
#         pontuacao += 10 * (4-tentativas)

# print("Sua pontuação final foi:", pontuacao)
# print("Fim de Jogo!")

while True:
    print('''
Sistema de RH Empresa XYZ

Escolha uma opção do menu abaixo:
          
          1. Ver Funcionários
          2. Adicionar Funcionário
          3. Remover Funcionário
          4. Alterar Cadastro de Funcionário
          0. Sair
''')
    op = input("Digite a opção desejada:")

    if (op == "1"):
        print("Executando o Ver Funcionários!")
    elif (op == "2"):
        print("Executando o Adicionar Funcionários!")
    elif (op == "3"):
        print("Executando o Remover Funcionários!")
    elif (op == "4"):
        print("Executando o Alterar Cadastro de Funcionários!")
    elif (op == "0"):
        print("Saindo do programa...")
        break
    else:
        print("Você digitou uma operação inválida!")

    input("DIGITE ENTER PARA CONTINUAR")

print("Fim do programa!")