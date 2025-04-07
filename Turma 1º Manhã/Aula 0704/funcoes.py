def hello():
    print("Hello World")

def helloAlternativo(nome):
    print(f"Hello {nome}")

helloAlternativo("Tarik")
helloAlternativo("Julia")
helloAlternativo("Hugo")
helloAlternativo("João Miguel")

#Crie uma função chamada hello2. Essa função deve pedir o nome do usuário e imprimir na tela "Hello, {nome}!" Teste a função, chamando-a 3 vezes.

def hello2():
    nome = input("Digite o nome do usuário: ")
    print(f"Hello, {nome}!")

# Modifique a função hello2 para exibir na tela "Digite o nome do usuário", quando pedir o nome, e imprimir ao final "Usuário Cadastrado: {nome}". Além disso peça a idade, a altura e o genero do usuário. Imprima essas informações no formato: 
"Idade: {idade}"
"Altura: {altura}"
"Gênero: {genero}"

def cadastroUsuario():
    print("-----CADASTRO DE USUÁRIO-----")
    
    nome = input("Digite o nome do usuário:")

    print(f"Usuário Cadastrado: {nome}")

    print("Informações Pessoais: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário: "))
    genero = input("Digite o gênero do usuário: ")
    
    print(f'''
    Idade: {idade} anos
    Altura: {altura} m
    Gênero: {genero}
''')
    
    


while (True):
    print("SISTEMA RH")

    print('''
Escolha uma opção do menu:
          1. Cadastrar Usuário
          2. Ver Usuários
          3. Remover Usuários
          0. Sair
''')
    opcao = input("Digite o número da opção desejada:")

    if (opcao == "1"):
        cadastroUsuario()
         
    elif(opcao == "0"):
        print("Saindo do Programa...")
        break
    else:
        print("Não implementado ainda...")