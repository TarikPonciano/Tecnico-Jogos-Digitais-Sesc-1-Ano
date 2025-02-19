print("Sistema Escolar")

print("Digite abaixo as notas pedidas:")

nota1 = float(input("Digite a nota da Prova 1:"))
nota2 = float(input("Digite a nota da Prova 2:"))
nota3 = float(input("Digite a nota da Prova 3:"))
nota4 = float(input("Digite a nota da Prova 4:"))

media = (nota1+nota2+nota3+nota4)/4

print(f"Media do aluno: {media:.1f}")

if (media >= 7 and media <= 10):
    print("Voce esta aprovado!")
elif (media >= 4 and media < 7):
    print("Voce esta de recuperacao!")
elif (media >= 0 and media < 4):
    print("Voce esta reprovado!")
else:
    print("Media invalida!")