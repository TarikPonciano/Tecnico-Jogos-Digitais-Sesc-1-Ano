pessoa = {
    "Nome": "Tarik",
    "Idade": 29,
    "Altura": 1.7
}
print(pessoa)

pessoa["Nacionalidade"] = "Brasileiro"

print(pessoa)

pessoa.pop("Altura", None)

print(pessoa)

print(f'''

Nome: {pessoa["Nome"]}
Idade: {pessoa["Idade"]}
Nacionalidade {pessoa["Nacionalidade"]}

''')


#Crie um cadastro de pet, de um petshop, esse cadastro precisa possuir as informações Nome, Espécie, Peso e Idade. Use um dicionário para armazenar essas informações e imprima na tela a ficha desse paciente pet.