#Crie um programa que pede as quatro notas de um aluno. Calcule a média desse aluno e exiba na tela se o aluno está aprovado ou reprovado. Média de aprovação é 7.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4

print(f"A média do aluno é {media:.2f}!")

if media >= 7:
    print("Parabéns, você foi aprovado por média!")
else:
    print("Que pena, você não foi aprovado")