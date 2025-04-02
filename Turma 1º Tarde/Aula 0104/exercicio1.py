nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
email = input("Digite seu email: ")

print(f"Bem-vindo(a) à nossa loja, {nome}! É um prazer ter você por aqui.")

pessoa = {
    "Nome": nome,
    "Idade": idade,
    "Email": email,
    "CPF": "12345678910"
}


print(f'''
Cadastro de Usuário:

      Nome: {pessoa["Nome"]}
      Idade: {pessoa["Idade"]}
      Email: {pessoa["Email"]}      

''')

print("Cadastro de Usuário")

for atributo in pessoa:
    print(f"{atributo}: {pessoa[atributo]}")