import utils

# Crie um programa de cadastro de funcionários que pede Nome, Cargo, Salário e Senha. Ao final do cadastro exiba as informações na tela de maneira formatada. Ex:
# Nome: João
# Cargo: Gerente
# Salário: R$ 5000,00
# Senha: 123456

nome = ""
cargo = ""
salario = 0.0
senha = ""

nome = input("Digite o nome do funcionário: ").upper()
cargo = input("Digite o cargo do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))

while (True):
    senha = input("Digite a senha do funcionário: ")
    senhaValida = utils.verificarSenha(senha)
    
    if (senhaValida):
        print("SENHA CONFIRMADA. PODE PROSSEGUIR!")
        break
    else:
        print("SENHA INVALIDA. A SENHA DEVE CONTER MAIUSCULO, MINUSCULO e PELO MENOS 6 CARACTERES!")

# Exiba uma mensagem dizendo "Bem vindo, {primeiroNome}." que usa o primeiro nome da pessoa da variável nome. Dica: Sabemos que o primeiro nome acabou quando encontramos " "

print(f"Bem vindo, {utils.extrairPrimeiroNome(nome)}!")

print(f'''
Nome: {nome}
Cargo: {cargo}
Salário: {utils.salarioFormatado(salario)}
Senha: {senha}
''')