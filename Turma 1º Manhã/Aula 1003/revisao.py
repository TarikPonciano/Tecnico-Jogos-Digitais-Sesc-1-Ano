nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Olá, meu nome é {nome}! E tenho {idade} anos!")

if (idade >= 60):
    print("Você é idoso!")
elif (idade >= 18 and idade < 60):
    print("Você é adulto!")
elif (idade >= 0 and idade < 18):
    print("Você é criança!")
else:
    print("Idade inválida!")

qtdAnimais = int(input("Digite quantos animais de estimação você possui: "))

animais = ""

for i in range(qtdAnimais):
    nomeAnimal = input("Digite o nome do seu animal de estimação: ")
    animais += nomeAnimal + " "

print("Seus animais de estimação:", animais)

while(True):
    print('''
    Escolha uma das opções:
          1. Imprimir seu nome na tela
          2. Imprimir sua idade na tela
          3. Imprimir nome dos animais na tela
          0. Sair
''')
    op = input("Digite uma das opções do menu: ")

    if op == "1":
        print(nome)
    elif op == "2":
        print(idade)
    elif op == "3":
        print(animais)
    elif op == "0":
        print("Finalizando o programa...")
        break
    else:
        print("Você digitou uma opção inválida!")

    input("Pressione Enter para continuar!")

