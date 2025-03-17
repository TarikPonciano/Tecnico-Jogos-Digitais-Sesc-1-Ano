# Crie um programa que contém uma lista vazia de funcionários.

# Faça com que o programa repita indefinidamente (while(true))

# A cada repetição exiba um menu com as opções "Ver lista", "Inserir novo funcionário", "Organizar lista alfabeticamente", "Sair"

# A opção "Ver Lista" deve exibir os funcionários na tela

# A opção "Inserir novo funcionário" deve pedir o nome de um funcionário e adiciona-lo à lista de funcionários. Bônus: Imprima na tela se o nome for repetido e não adicione na lista

# A opção "Ordernar alfabeticamente" deve rodar o comando lista.sort()

# A opção "Sair" encerra o programa
funcionarios = []

while True:
    print('''
BEM VINDO AO GERENCIAMENTO RH

          MENU:
          1. VER LISTA DE FUNCIONÁRIOS
          2. ADICIONAR NOVO FUNCIONÁRIO
          3. ORGANIZAR LISTA ALFABETICAMENTE
          0. SAIR    


''')
    op = input("Digite a opção desejada: ")

    if (op == "1"):
        print(f"Lista de funcionarios: {funcionarios}")
    elif (op == "2"):
        print("INSERINDO FUNCIONÁRIO")
        novoFuncionario = input("Digite o nome do novo funcionário: ")
        if (novoFuncionario in funcionarios):
            print("NOME DUPLICADO! NOME NÃO INSERIDO!")
        else:
            funcionarios.append(novoFuncionario)
        
    elif (op == "3"):
        print("LISTA ORGANIZADA!")
        funcionarios.sort()
    elif (op == "0"):
        print("Finalizando Programa....")
        break
    else: 
        print("Você digitou uma opção inválida!")

    
    input("TECLE ENTER PARA CONTINUAR!")