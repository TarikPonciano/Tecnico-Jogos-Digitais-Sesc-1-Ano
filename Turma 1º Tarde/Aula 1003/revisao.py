# Crie as variáveis nome e idade e atribua valores a essas variáveis

# Imprima na tela uma mensagem de saudação "Olá meu nome é {nome} e tenho {idade} anos!"

# Modifique o programa para pedir ao usuário as informações nome e idade

# Crie uma verificação para checar se a pessoa é maior de idade


nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))


print(f"Olá meu nome é {nome} e tenho {idade} anos!")



# Melhore a verificação de idade. Agora verifique se a pessoa é idosa (idade maior ou igual a 60), adulta (idade maior ou igual a 18 e menor que 60) ou jovem (idade menor que 18)
if idade >= 60:
    print("Você é idose!")
elif idade >= 18 and idade < 60:
    print("Você é adulte!")
elif idade < 18 and idade >= 0:
    print("Você é jovem!")
else:
    print("Você é um alienigene")

# Pergunte para o usuário quantos animais de estimação ele tem. Na sequencia pergunte o nome de cada animal, utilizando repetição. Ao final, exiba o nome dos animais de estimação informados.

qtdAnimais = int(input("Digite quantos animais de estimação você possui:"))
animais = ""
for i in range(qtdAnimais):
    nomeAnimal = input("Digite o nome de seu animal de estimação: ")
    animais += nomeAnimal + " "

print(animais)

# Exiba na tela um menu que contém as opções:

# 1. Ver nome completo
# 2. Ver idade
# 3. Ver animais
# 4. Ver todas as informações cadastradas (nome,idade,animais)
# 0. Sair

# Este programa deve pedir para o usuário escolher uma opção da lista, exibir a informação indicada na opção e deve repetir sua execução até que a pessoa escolha SAIR.