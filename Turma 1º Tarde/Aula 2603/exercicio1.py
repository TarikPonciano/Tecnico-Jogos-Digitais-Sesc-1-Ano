nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
email = input("Digite seu email: ")

if (idade >= 18):
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")

print(f"Seja bem vindo, {nome}! Uma mensagem de confirmação foi enviada para seu email {email}")