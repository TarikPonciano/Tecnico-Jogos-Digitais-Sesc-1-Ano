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


print("Bem vindo ao XYZ")

while (True):

    print('''
    Escolha uma opção do menu:
        
        1. Ver nome cadastrado
        2. Ver idade cadastrada
        3. Ver pets cadastrados
        4. Ver todas as informações
        0. Sair

    ''')

    op = input("Digite a opção desejada do menu:")

    if (op == "1"):
        print(f"Nome cadastrado: {nome}")
    elif (op == "2"):
        print(f"Idade cadastrada: {idade} anos")
    elif (op == "3"):
        print(f"Seus pets cadastrados são: {animais}")
    elif (op == "4"):
        print("PERFIL DO USUÁRIO")

        print(f"Nome cadastrado: {nome}")
        print(f"Idade cadastrada: {idade} anos")
        print(f"Seus pets cadastrados são: {animais}")
    elif (op == "0"):
        print("Saindo do Programa...")
        break
    else:
        print("Escolha uma opção válida!")

    input("PRESSIONE ENTER")