#Crie um aplicativo de termômetro que pede a temperatura da pessoa (float) e informa o nível de febre da pessoa. Se a pessoa estiver com temperatura menor ou igual a 36.5, está sem febre. Se a pessoa estiver com temperatura maior que 36.5 e menor ou igual a 37.5 a pessoa está com febre baixa. Se a pessoa estiver com mais que 37.5, ela está com febre alta, encaminhar para emergência.

temperatura = float(input("Digite sua temperatura atual: "))

if temperatura < 36:
    print("Você está com hipotermia!")
elif temperatura >= 36 and temperatura <= 37.5:
    print("Você está sem febre!")
elif temperatura > 37.5 and temperatura <=39.5:
    print("Você está com febre!")
elif temperatura > 39.5 and temperatura <= 41:
    print("Voc~e está com febre alta!")
elif temperatura > 41:
    print("Você está com HIPERTERMIA")
else:
    print("Algo deu errado!")