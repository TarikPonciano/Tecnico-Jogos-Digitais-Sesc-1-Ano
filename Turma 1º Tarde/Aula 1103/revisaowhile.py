convidados = []

while(True):
    convidado = input("Digite o nome de um convidado (PARA SAIR DIGITE 'SAIR'):")

    if convidado == "SAIR":
        print("Encerrando Programa...")
        break
    else:
        convidados.append(convidado)

convidados[2] = "Amanda"
print(convidados)