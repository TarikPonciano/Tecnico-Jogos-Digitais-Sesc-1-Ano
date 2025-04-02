'''
1. Criar variáveis e guardar informação
2. Utilizar comandos de inserção de informação
3. Tipos de dados
4. Estruturas de Condição
5. Estruturas de Repetição
6. Coleções
7. Funções
8. Programação Orientada a Objetos
'''
autorizados = []

while True:
    nome = input("Digite o seu nome: ")

    if nome == "sair":
        print("Encerrando o programa...")
        break

    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))

    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Altura: {altura:.2f}m")

    # Para andar no insano a pessoa precisa ser maior que 1.5m ou ter mais que 15 anos

    if altura >= 1.5 and idade >= 15:
        print("Você está liberado para descer no insano!") 
        autorizados.append(nome)
    elif altura < 1.5:
        print("Você é baixe demais para descer o Insano!")
    elif idade < 15:
        print("Você é novu demais para descer o Insano!")
    else:
        print("Algo estranho aconteceu!")



print("Lista de autorizados:", autorizados)