from classesVeiculos import Veiculo, Trem, Navio, Aviao

veic1 = Veiculo("Bis 100", "Honda", "PNZ-5X23", 100, "Terrestre")

veic1.desacelerar()
veic1.desacelerar()
veic1.desacelerar()
veic1.desacelerar()
veic1.desacelerar()

veic1.parar()

veic1.desacelerar()

veic1.mostrarInformacoes()

veic2 = Trem("Southern Pacific 4449", "Lima Locomotives Works", "123141412412", 180)
veic2.acelerar()
veic2.desacelerar()
veic2.mostrarInformacoes()

veic3 = Aviao("Boeing-767", "Boeing", "767-3245", 300)

veic3.mostrarInformacoes()


veic3.decolar()
