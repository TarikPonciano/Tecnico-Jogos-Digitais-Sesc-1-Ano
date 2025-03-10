# Crie as variáveis nome e idade e atribua valores a essas variáveis

# Imprima na tela uma mensagem de saudação "Olá meu nome é {nome} e tenho {idade} anos!"

# Modifique o programa para pedir ao usuário as informações nome e idade

# Crie uma verificação para checar se a pessoa é maior de idade


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Olá meu nome é {nome} e tenho {idade} anos!")



# Melhore a verificação de idade. Agora verifique se a pessoa é idosa (idade maior ou igual a 60), adulta (idade maior ou igual a 18 e menor que 60) ou jovem (idade menor que 18)
if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")
