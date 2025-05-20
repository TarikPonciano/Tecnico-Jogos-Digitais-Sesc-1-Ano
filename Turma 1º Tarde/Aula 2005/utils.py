def extrairPrimeiroNome(nome):
    primeiroNome = ""

    for letra in nome:
        if (letra == " "):
            break
        primeiroNome += letra

    return primeiroNome
    

def salarioFormatado(salario):
    if salario < 1000000:
        return f"R$ {salario:.2f}"
    else:
        salario = salario/1000000
        return f"R$ {salario:.2f} Mi"
    
def validarSenha(senha):

    temMaiuscula = False
    temMinuscula = False
    tem6Caracteres = len(senha) >= 6

    for caractere in senha:
        
        if caractere in "1234567890!@#$%¨&*()":
            continue

        if caractere == caractere.upper():
            temMaiuscula = True

        if caractere == caractere.lower():
            temMinuscula = True

        if temMaiuscula and temMinuscula:
            break

    return temMaiuscula and temMinuscula and tem6Caracteres