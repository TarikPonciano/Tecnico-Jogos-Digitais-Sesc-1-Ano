# Crie um programa que, usando loop for, pede 4 notas de um aluno. Calcule a soma dessas notas, a média dessas notas e exiba a média final e a situação do aluno seguindo as regras abaixo:
#Se o aluno tirou um nota maior ou igual a 7 e menor ou igual a 10, ele está aprovado.
#Se não, se o aluno tirou uma nota maior ou igual a 4 e menor que 7, o aluno está de recuperação.
#Se não, se o aluno tirou uma nota maior ou igual a 0 e menor que 4, o aluno está reprovado.
#Caso a média seja diferente de todas essas opcoes, a média é inválida
soma = 0

for i in range(4):
    nota = float(input("Digite uma nota:"))
    soma += nota

media = soma / 4

print(f"Sua média final foi: {media}")

if (media >= 7 and media <= 10):
    print("Você está aprovado!")
elif (media >= 4 and media < 7):
    print("Você está de recuperação!")
elif (media >= 0 and media < 4):
    print("Você está reprovado!")
else:
    print("Média inválida!")
