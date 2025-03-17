# Crie um programa que contém uma lista vazia de funcionários.

# Faça com que o programa repita indefinidamente (while(true))

# A cada repetição exiba um menu com as opções "Ver lista", "Inserir novo funcionário", "Organizar lista alfabeticamente", "Sair"

# A opção "Ver Lista" deve exibir os funcionários na tela

# A opção "Inserir novo funcionário" deve pedir o nome de um funcionário e adiciona-lo à lista de funcionários. Bônus: Imprima na tela se o nome for repetido e não adicione na lista

# A opção "Ordernar alfabeticamente" deve rodar o comando lista.sort()

# A opção "Sair" encerra o programa

funcionarios = []

while(True):
    
    print('''
Bem vindo à GERENCIAMENTO RH
          Menu:
          1. Ver Funcionários
          2. Adicionar Funcionário
          3. Organizar alfabeticamente
          0. Sair

          
''')
    op = input("Digite o número da opção desejada:")

    if (op == "1"):
        print("Lista de funcionarios:", funcionarios)