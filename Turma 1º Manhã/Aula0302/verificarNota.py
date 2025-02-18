# Crie um programa que pede a nota de um aluno. Se a nota for maior ou igual a 7, deverá imprimir a mensagem de que ele está aprovado, se não, deverá imprimir que o aluno está reprovado.

#Dica: A varíavel nota deve ser float

#Agora peça 4 notas do mesmo aluno e calcule sua média
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4)/4

if (media >= 7):
    print("Parabéns, você está aprovado!")
else:
    print("Que pena, você está reprovado!")

print(f"Sua média foi: {media:.2f}")