# Você foi contratado para desenvolver o GERENCIADOR DE RH 2000. Você deverá criar um software que gerencia uma lista de funcionários de uma determinada empresa.

# Primeiro passo do programa: Crie uma lista chamada funcionarios que contém o nome de 5 funcionários
funcionarios = ["Mauricio", "Vinicius", "Renan", "Vlauber", "Matheus"]

# Exiba o funcionário na posição 4 e imprima "Funcionário do mês: {funcionario4}"

print(f"Funcionário do mês: {funcionarios[4]}")

# Mudar o nome do funcionario na posição 1 e imprimir a lista completa

funcionarios[1] = "Isadora"
print(funcionarios)

# Insira um novo funcionário na lista (append) e exiba a lista completa
funcionarios.append("Isaac")

print(funcionarios)

# Peça para que o usuário escreva um nome e também insira (append) na lista de funcionários
novoFuncionario = input("Digite o nome de um novo funcionário: ")
funcionarios.append(novoFuncionario)

print(funcionarios)

# Melhore o trecho anterior para que seja repetido 5 vezes

for i in range(5):
    novoFuncionario = input("Digite o nome de um funcionário: ")
    funcionarios.append(novoFuncionario)

print(funcionarios)

# Remova da lista de funcionários o primeiro funcionário da lista e o último funcionário da lista. Imprima a lista resultante ao final. Bônus: Para cada funcionario removido imprima "{funcionario} foi demitido!"

print(f"Funcionário demitido: {funcionarios.pop(0)}")


print(f"Funcionário demitido: {funcionarios.pop()}")

print(funcionarios)


# Organize alfabeticamente sua lista de funcionários

funcionarios.sort()
print(funcionarios)
