# Crie um programa de cadastro de manga (quadrinhos japoneses). Identifique pelo menos 4 informações a serem armazenadas do manga e guarde essas informações em um dicionário. Ao final exiba o dicionário.
listaMangas = []

while True:
    nomeManga = input("Digite o nome do Manga:")
    valorManga = float(input("Digite o valor do Manga:"))
    autorManga = input("Digite o autor do Manga:")
    tamanhoManga = input("Digite o tamanho do Manga:")

    if (valorManga < 10):
        print("VALOR INVÁLIDO")
    else:
        dicionarioManga = {
            "Nome": nomeManga,
            "Valor": valorManga,
            "Autor": autorManga,
            "Tamanho": tamanhoManga
        }

    listaMangas.append(dicionarioManga)

    if (input("Digite S para sair") == "S"):
        break


print("Lançamentos:")

for manga in listaMangas:
    print(f'''
 
    Nome: {manga["Nome"]}
    Valor: {manga["Valor"]}
    Autor: {manga["Autor"]}
    Tamanho: {manga["Tamanho"]}

''')

# Agora crie uma lista de mangas e cada novo manga registrado, guarde na lista.