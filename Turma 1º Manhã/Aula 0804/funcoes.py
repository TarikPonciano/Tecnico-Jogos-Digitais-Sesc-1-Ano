def helloWorld():
    print("Hello World")

def hello(n):
    print(f"Olá, {n}!")

def saudacao(nome, idade, altura):
    print(f'''Olá, me chamo {nome}! 
          
Tenho {idade} anos e {altura} metros de altura.''')
    print("---------------------------")

def exibirAlunos(listaAlunos):
    listaAlunos.sort()
    contador = 1
    print("LISTA DE ALUNOS")
    for aluno in listaAlunos:
        print(f"{contador}. {aluno}")
        contador += 1



notas = [5,8,9,10,7]

print(sum(notas))


