class Pet():
    def __init__(self, nome, idade, peso, especie, raca, dono):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.especie = especie
        self.raca = raca
        self.dono = dono
    

animal1 = Pet("Lulu", 17, 25, "Cachorro", "Poodle", "Luana")

animal2 = Pet("Neymarzinho", 5, 3, "Cachorro", "Poodle", "Marco Antonio")

animal3 = Pet(dono="Tarik", idade=2, peso=3.4, especie="Gato", raca= "SRD", nome="Luna")

print(f"{animal1.nome} - {animal1.especie} - {animal1.raca}")
print(f"{animal2.nome} - {animal2.especie} - {animal2.raca}")


# Criar um programa veterinário que contém a classe Pet. Cada animal do tipo Pet, deve ter nome, idade, peso, espécie, raça, nome do dono. Depois de criar a classe, instancie 3 animais diferentes e imprima na tela o nome, idade e peso de cada um.

# - Criar a class Pet
# - Criar o construtor (__init__) e definir os atributos (nome, idade, peso, especie, raça, dono)
# - Fora da classe, criar 3 elementos usando a classe Pet.
#   Ex: animal1 = Pet('Fluffy', 7, 4, 'coelho', 'branco', 'Maicao')