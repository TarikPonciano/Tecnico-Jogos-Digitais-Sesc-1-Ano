# Crie uma classe Animal que contém pelo menos 5 informações. Crie 3 animais diferentes usando a classe Animal e exiba na tela as informações completas de cada animal.

class Animal:
    def __init__(self, especie, peso, altura, raca, habitat):
        self.especie = especie
        self.peso = peso
        self.altura = altura
        self.raca = raca
        self.habitat = habitat
    def mostrarInformacoes(self):
        print(f'''
----- Informações Pet -----
              
    Espécie: {self.especie}
    Peso: {self.peso} Kg
    Altura: {self.altura} m
    Raça: {self.raca}
    Habitat: {self.habitat}

''')

animal1 = Animal("Guaxinim", 5, 0.3, "Americano", "Urbano")
animal2 = Animal("Gato", 3.5, 0.4, "Pé Duro", "Apartamento")
animal3 = Animal("Calopsita", 0.2, 0.1, "Amarela", "Coqueiro" )

# animal1.mostrarInformacoes()
# animal2.mostrarInformacoes()
# animal3.mostrarInformacoes()

print(f'''
----- Informações Pet -----
              
    Espécie: {animal1.especie}
    Peso: {animal1.peso} Kg
    Altura: {animal1.altura} m
    Raça: {animal1.raca}
    Habitat: {animal1.habitat}

''')

print(f'''
----- Informações Pet -----
              
    Espécie: {animal2.especie}
    Peso: {animal2.peso} Kg
    Altura: {animal2.altura} m
    Raça: {animal2.raca}
    Habitat: {animal2.habitat}

''')

print(f'''
----- Informações Pet -----
              
    Espécie: {animal3.especie}
    Peso: {animal3.peso} Kg
    Altura: {animal3.altura} m
    Raça: {animal3.raca}
    Habitat: {animal3.habitat}

''')