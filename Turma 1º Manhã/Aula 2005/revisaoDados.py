from classPessoa import Pessoa

nome = "Fulano"
idade = 20
altura = 1.75
peso = 70.5



pessoaLista = [nome, idade, altura, peso]

pessoaLista[0] #nome

pessoaDicionario = {
    "Nome": nome,
    "Idade": idade,
    "Altura": altura,
    "Peso": peso
}

pessoaDicionario["Nome"] #nome
pessoaDicionario["Idade"] = "Abacate"
pessoaDicionario["CPF"] = "abcdefgh"


pessoa1 = Pessoa(nome, 30, altura, peso)

print(pessoa1.idade)
print(pessoa1.faixaEtaria)

pessoa1.mostrarInformacoes()

pessoa2 = Pessoa("Victoria", 16, 1.61, 60)

pessoa2.mostrarInformacoes()