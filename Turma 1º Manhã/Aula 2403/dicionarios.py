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


#Crie um cadastro de pet, de um petshop, esse cadastro precisa possuir (usar input) as informações Nome, Espécie, Peso e Idade. Use um dicionário para armazenar essas informações e imprima na tela a ficha desse paciente pet.

pet = {

}

pet["Nome"] = input("Digite o nome do pet: ")
pet["Espécie"] = input("Digite a espécie do seu pet: ")
pet["Peso"] = float(input("Digite o peso do seu pet:"))
pet["Idade"] = int(input("Digite a idade do seu pet: "))
pet["Tutor"] = input("Digite seu nome:")

print(f'''
Ficha do Paciente:
      

      Nome - {pet["Nome"]}
      Espécie - {pet["Espécie"]}
      Peso - {pet["Peso"]}
      Idade - {pet["Idade"]}

''')


#Impressão automática de informações do dicionário
# for key in pet.keys():
#     print(f"{key} - {pet[key]}")