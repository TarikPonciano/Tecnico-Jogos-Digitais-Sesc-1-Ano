# Crie um programa que pede a temperatura em Fahrenheits, para calcular e exibir na tela um resultado em Celsius.
#Formula > celsius = (tempF - 32) * (5/9)
tempF = input("Digite a temperatura em Fº:")
tempF = float(tempF)

tempC = (tempF - 32) * (5 / 9)
print(f"A temperatura em ºC eh {tempC:.1f} graus!")

