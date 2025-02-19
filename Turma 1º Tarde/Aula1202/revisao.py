print('''
Lista de Personagens:
      
1. Goku
2. Vegeta
3. Gohan
4. Yamcha
5. Broly

''')
personagem = input("Digite o numero de um personagem:")

if (personagem == "1"):
    print("O poder de luta do Goku eh mais de 8000!")
elif (personagem == "2"):
    print("O poder de luta do Vegeta eh 7000")
else:
    print("Voce escolheu um numero invalido! Escolha novamente!")