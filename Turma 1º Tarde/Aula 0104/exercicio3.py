tarefas = []
diasDaSemana =["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

for dia in diasDaSemana :
    novaTarefa = input(f"Digite a tarefa da {dia}: ")
    tarefas.append(novaTarefa)

print("Lista de Tarefas")

for i in range(5): #Poderia usar range(len(tarefas))
    print(f"{diasDaSemana[i]} - {tarefas[i]}")