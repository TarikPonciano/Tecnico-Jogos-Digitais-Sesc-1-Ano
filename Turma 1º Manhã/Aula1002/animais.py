#Faça um programa que recebe o nome de um animal. Se o animal for cachorro imprime "Au au". Se o animal for gato imprime "Miau". Se o animal for papagaio imprime "Lôro quer biscoito". Se o animal não for identificado imprime "Animal silvestre detectado, chame o ibama."

animal = input("Digite o nome do animal:")

if animal == "cachorro":
    print("O cachorro faz Au Au")
elif animal == "gato":
    print("O gato faz MIAAAAAAAAUUUU")
elif animal == "papagaio":
    print("O papagaio faz Lôro quer Biscoito")
elif animal == "tartaruga":
    print("A tartaruga faz AAAAAANNNNNNN")
else:
    print("Animal não identificado. As autoridades foram contactadas!")