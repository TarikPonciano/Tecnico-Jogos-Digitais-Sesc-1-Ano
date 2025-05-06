extends Node2D

func _ready() -> void:
	#Crie um programa de calculadora que utiliza um número1, número2 e operação.
	#Esse programa deve suportar as operações (+,-,*,/)
	#Ao executar o programa deve ler os dois números e operação e exibir na tela
	#uma mensagem e resultado correspondentes. Exemplo:
	#ENTRADAS:
		#numero1 = 20
		#numero2 = 30
		#operacao = "+"
	#SAÍDA: "Resultado da Soma: 50"
	
	var numero1 = 300
	var numero2 = 50
	var op = "/"
	
	if (op == "+"):
		print("Resultado da Soma: ", (numero1+numero2))
	elif (op == "-"):
		print("Resultado da Subtração: ", (numero1-numero2))
	elif (op == "*"):
		print("Resultado da Multiplicação: ", (numero1*numero2))
	elif (op == "/"):
		if (numero2 == 0):
			print("DIVISÃO POR 0 NÃO AUTORIZADA!")
		else:
			print("Resultado da Divisão: ", (float(numero1)/float(numero2)))
	
