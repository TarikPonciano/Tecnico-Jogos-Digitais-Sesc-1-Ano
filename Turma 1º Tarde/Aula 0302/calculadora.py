# Crie um programa que declara 2 variáveis de números inteiros e exibe na tela a soma desses números. Imprima na tela a seguinte mensagem: "Soma: {resultado}"

print("Sejam bem vindo à")
print("----- MINHA CALCULADORA -----")

#Agora configure o programa para PEDIR os dois números inteiros
#Dica: lembrar de converter para int
num1 = int(input("Digite o número 1: "))
num2 = int(input("Digite o número 2: "))

#Realize as operações soma, subtração, multiplicação e divisão
soma = num1 + num2
print("O resultado da soma é:")
print(f"{num1} + {num2} = {soma}")

subtracao = num1 - num2
print("O resultado da subtracao é:")
print(f"{num1} - {num2} = {subtracao}")

multiplicacao = num1 * num2 
print("O resultado da multiplicação é: ")
print(f"{num1} x {num2} = {multiplicacao}")

divisao = num1 / num2 
print("O resultado da divisão é: ")
print(f"{num1} / {num2} = {divisao}")


