extends Node2D


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	#Crie um programa que recebe dois números decimais e uma operação (+,-,*,/)
	#Dependendo da operação escolhida. Exiba no terminal o resultado dessa operação entre os dois números. Exemplo:
	
	#Entradas:
	#	n1 = 20
	#	n2 = 30
	#	op = "-"
	
	#Saídas:
	#	"Resultado da Subtração: -10"
	var n1 = 5.0
	var n2 = 0
	var op = "/"
	
	if (op == "+"):
		print("Resultado da Soma: ",(n1+n2))
	elif (op == "-"):
		print("Resultado da Subtração: ",(n1-n2))
	elif (op == "*"):
		print("Resultado da Multiplicação: ",(n1*n2))
	elif (op == "/"):
		#Impeça o acontecimento de divisões por 0
		if (n2 == 0):
			print("DIVISÃO POR 0 IDENTIFICADA! ABORTAR!")
		else:
			print("Resultado da Divisão: ",(float(n1)/float(n2)))
	else:
		print("ESCOLHA UMA OPERAÇÃO VÁLIDA")
	
	
