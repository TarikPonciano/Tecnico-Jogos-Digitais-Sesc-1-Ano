#Verificar a idade de um usuário para checar se é permitido a ele assistir "Jogos Mortais"

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você foi autorizado a assistir Jogos Mortais! Aproveite o filme!")
    print(f"Sua idade é {idade} anos!")
else:
    print("Você não tem idade suficiente para assistir o filme!")


print("Até mais!")