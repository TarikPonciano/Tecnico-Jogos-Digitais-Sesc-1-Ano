def eh_primo(numero):
    cont_divisores = 0
    cont_numeros = 1x


    while cont_numeros <= numero:
        if numero % cont_numeros == 0:  # Verifica se é divisor
            cont_divisores += 1
        cont_numeros += 1 

    # Se o número tiver exatamente dois divisores (1 e ele mesmo), é primo
    if cont_divisores == 2:
        print("Primo")
    else:
        print("Não é primo")

# Entrada do número
numero = int(input("Digite um número: "))
eh_primo(numero)
