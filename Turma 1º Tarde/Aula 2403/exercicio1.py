# 1. Peça o nome de um usuário e imprima na tela a primeira e última letra do nome

nome = input("Digite seu nome:")
 
primeiraLetra = nome[0]
ultimaLetra = nome[-1]

print(f'''

Primeira Letra: {primeiraLetra}

Última Letra: {ultimaLetra}

''')

vogais = ["a", "e", "i", "o", "u"]

if (nome[0].lower() in vogais):
    print("O nome começa com vogal!")
else:
    print("O nome começa com uma consoante!")