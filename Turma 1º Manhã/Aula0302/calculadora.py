#Crie um programa de calculadora que executa os passos a seguir:
#https://dontpad.com/gamesesc
print("BEM VINDO À")
print("----- MINHA CALCULADORA -----")

#Peça ao usuário para fornecer os dois números
#Dica int(input("Mensagem"))
num1 = int(input("Digite o número 1: "))
num2 = int(input("Digite o número 2: "))

#Agora faça soma, subtração, multiplicação e divisão
soma = num1 + num2 
print("O resultado da soma é:")
print(f"{num1} + {num2} = {soma}")

subtracao = num1 - num2 
print("O resultado da subtração é:")
print(f"{num1} - {num2} = {subtracao}")

multiplicacao = num1 * num2
print("O resultado da multiplicação é:")
print(f"{num1} x {num2} = {multiplicacao}")

divisao = num1 / num2
print("O resultado da divisão é:")
print(f"{num1} / {num2} = {divisao}")