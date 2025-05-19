def extrairPrimeiroNome(nomeCompleto):
    nome1 = ""
    for letra in nomeCompleto:
        if (letra == " "):
            if (nome1 != ""):
                break
        else:
            nome1 += letra

    return nome1 

def salarioFormatado(salario):

    if (salario < 1000000):
        salarioFormatado = f"R$ {salario:.2f}"
    else:
        salario = salario/1000000
        salarioFormatado = f"R$ {salario:.1f} milhões"

    return salarioFormatado

def verificarSenha(senha):
    temMaiuscula = False
    temMinuscula = False
    tem6Caracteres = len(senha) >= 6
    
    for caractere in senha:
        if caractere in "1234567890":
            continue
        
        if caractere == caractere.upper():
            temMaiuscula = True
        
        if caractere == caractere.lower():
            temMinuscula = True

        if temMinuscula and temMaiuscula:
            break
    
    return temMaiuscula and temMinuscula and tem6Caracteres