# Peça o nome de um usuário e imprima na tela a primeira e última letra do nome
nome = input("Digite o nome de um usuário: ")
print(f"Primeira letra do nome: {nome[0]}")
print(f"Ultima letra do nome: {nome[-1]}")

vogais = ("a","e","i","o","u")

if (nome[0].lower() in vogais):
    print("Seu nome começa com vogal!")
else:
    print("Seu nome começa com consoante!")
