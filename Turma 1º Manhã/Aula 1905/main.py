# Crie um programa de cadastro de funcionários que pede Nome, Cargo, Salário e Senha. Ao final do cadastro exiba as informações na tela de maneira formatada. Ex:
# Nome: João
# Cargo: Gerente
# Salário: R$ 5000,00
# Senha: 123456

nome = ""
cargo = ""
salario = 0.0
senha = ""

nome = input("Digite o nome do funcionário: ")
cargo = input("Digite o cargo do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))
senha = input("Digite a senha do funcionário: ")

# Exiba uma mensagem dizendo "Bem vindo, {primeiroNome}." que usa o primeiro nome da pessoa da variável nome. Dica: Sabemos que o primeiro nome acabou quando encontramos " "

print(f'''
Nome: {nome}
Cargo: {cargo}
Salário: R$ {salario:.2f}
Senha: {senha}
''')