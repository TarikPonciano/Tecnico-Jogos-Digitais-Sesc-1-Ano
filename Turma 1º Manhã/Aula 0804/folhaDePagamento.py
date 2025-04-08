def calcularPagamento(horasTrabalhadas, valorHora):
    horas = float(horasTrabalhadas)
    valor = float(valorHora)

    if (horas <= 40):
        salario = horas * valor
    else:
        horasExtras = horas - 40
        salario = (40 * valor) + (horasExtras * (1.5 * valor))

    return salario

print("----- FOLHA DE PAGAMENTO ------")

print("Insira sua informações para calcular seu salário da semana!")

h = input("Digite quantas horas trabalhou:")
v = input("Digite o valor de cada hora trabalhada:")

salarioFinal = calcularPagamento(h, v)

print(f"O seu salário final da semana é: R$ {salarioFinal:.2f}")

