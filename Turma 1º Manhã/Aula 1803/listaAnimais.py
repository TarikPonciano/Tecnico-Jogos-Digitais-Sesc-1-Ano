# Crie uma lista de animais e insira na lista 7 espécies de animais diferentes, depois imprima na tela.
animais = ["Tatu", "Cachorro", "Gato", "Tartaruga", "Lobo", "Leão", "Kakapo", "Macaco", "Soin"]

print(f'''
Lista de Animais Versão 1:
''')

for i in range(len(animais)):
    print(f"{i+1}. {animais[i]}")

print(f'''
Lista de Animais Versão 2:
''')

contador = 1
for animal in animais:
    print(f"{contador}. {animal}")
    contador += 1