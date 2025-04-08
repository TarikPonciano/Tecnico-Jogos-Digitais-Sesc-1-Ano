def calcularPagamento(horas, valor):
    horas = float(horas)
    valor = float(valor)

    if (horas <= 40):
        salario = horas * valor
    else:
        extra = horas - 40
        salario = 40 * valor + (extra * (1.5*valor))
    
    return salario

print("----- FOLHA DE PAGAMENTO -----")
print("Forneça suas informações de carga horária para calcular seu salário!")

horasTrabalhadas = input("Digite quantas horas trabalhou: ")
valorHora = input("Digite quanto custa cada hora de trabalho: ")

salarioFinal = calcularPagamento(horasTrabalhadas, valorHora)

print(f"O seu total a receber esta semana é: R$ {salarioFinal:.2f}")