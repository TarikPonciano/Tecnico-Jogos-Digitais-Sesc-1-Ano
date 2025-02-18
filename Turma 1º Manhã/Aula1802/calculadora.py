#Crie um programa que pede ao usuário dois números decimais e uma operação matemática (+, -, *, /). Ao receber as informações o programa executa e exibe o resultado da operação escolhida. Ex:

#Usuário insere 10 e 30, escolhe a opção '*'. É exibido na tela: 'O resultado da multiplicação é: 300'.

#Alternativo: 'Resultado: 10 x 30 = 300'

num1 = float(input("Digite o primeiro número: "))

operacao = input("Escolha uma operação matemática (+, -, * /): ")

num2 = float(input("Digite o segundo número: "))

if (operacao == "+"):
    resultado = num1 + num2
elif (operacao == "-"):
    resultado = num1 - num2
elif (operacao == "*"):
    resultado = num1 * num2
elif (operacao == "/"):
    if(num2 == 0):
        resultado = "Divisão por Zero!!!!"
    else:
        resultado = num1 / num2
else:
    resultado = "Operação Inválida"


print(f"Resultado: {num1} {operacao} {num2} = {resultado}")


