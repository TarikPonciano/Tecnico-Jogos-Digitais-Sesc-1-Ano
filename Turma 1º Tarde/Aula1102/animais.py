#dontpad.com/gamesesc

#Crie um programa que pede ao usuário o nome de um animal.
#Se o animal for "cachorro", imprimir na tela Au Au
#Se o animal for "gato", MIAAAAAAAAuuuu
#Se o animal for "papagaio", Lôro quer biscoito
#Se o animal for "tartaruga", AAAAAAAANNNNNNN
#Se não for nenhum dos anteriores, acionar as autoridades do Ibama

animal = input("Digite o nome do animal: ").lower()
if animal == "cachorro":
    print("O cachorro faz 'Au Au lobinho'")
elif animal == "gato":
    print("O gato faz 'Miaaaaaau'")
elif animal == "papagaio":
    print("O papagaio faz 'Lôro quer biscoito'")
elif animal == "tartaruga":
    print("A tartaruga faz 'AAAAAAAAnnnnn'")
else:
    print("Animal não identificado. IBAMA CONTACTADO.")

