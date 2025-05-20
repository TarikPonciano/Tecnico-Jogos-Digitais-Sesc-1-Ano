import utils
print("Seja Bem Vindo ao Sistema XYZ")

nomeCompleto = input("Digite o nome completo do funcionário:")
cargo = input("Digite o cargo do funcionário:")
salario = float(input("Digite o salário do funcionário:"))
email = input("Digite o email do funcionário:")

while True:
    senha = input("Digite a senha do funcionário:")

    if (utils.validarSenha(senha)):
        break
    else:
        print("Senha inválida! Tente novamente!")

primeiroNome = utils.extrairPrimeiroNome(nomeCompleto)

print(f"Seja bem vindo, {primeiroNome}!")


print(f'''
Informações Pessoais:
            
Nome: {nomeCompleto}
Cargo: {cargo}
Salário: {utils.salarioFormatado(salario)}
Email: {email}
Senha: {senha}

''')

