# Você está criando um software de gerenciamento de funcionários para a empresa XYZ. Para criar o software siga as instruções abaixo:

# Declare uma lista chamada funcionários, que contém o nome de 5 funcionários.

funcionarios = ["Tarik", "Hugo", "Julio", "Marco", "Julia"]

# Imprima na tela o funcionário da posição 4

print(f"Funcionário do mês: {funcionarios[4]}")

# Acrescente um novo funcionário na lista e imprima a lista completa

funcionarios.append("Isabelly")
print(funcionarios)

# Peça para o usuário escrever o nome de um novo funcionário e acrescente esse nome na lista.

novoFuncionario = input("Digite o nome do novo funcionário:")
funcionarios.append(novoFuncionario)

# Melhore o código para agora pedir o nome de 5 novos funcionários e acrescente todos eles na lista.

for i in range(5):
    novoFuncionario = input("Digite o nome do novo funcionário:")
    funcionarios.append(novoFuncionario)

# Organize os nomes da lista em ordem alfabética (pesquisar o comando sort) e imprima a lista completa na tela.

funcionarios.sort()
print(funcionarios)

# Remova o primeiro nome da lista e remova o último nome da lista. Após realizar essas remoções, exibir a nova lista na tela.

funcionarios.pop(0)
funcionarios.pop()

print(funcionarios)

# Peça para o usuário um número de funcionário e mude o nome nessa posição

numero = int(input("Digite a posição que deseja alterar: "))

funcionarios[numero] = input("Digite o novo nome de funcionário:")

print(funcionarios)