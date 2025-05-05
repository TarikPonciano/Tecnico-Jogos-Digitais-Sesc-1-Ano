extends Node2D

func _ready() -> void:
	print("Hello World")
	#Crie um programa dentro do func _ready
	#Esse programa deve conter uma variável nome,
	#uma variável anoNascimento e uma variável idade
	#Na variável nome, preencha seu nome
	#Na variável anoNascimento, preecha seu ano de nascimento
	#Na variável idade, calcule a sua idade utilizando o ano de nascimento informado
	#Exiba ao final uma mensagem contendo o nome e idade do usuário
	
	var nome = "Tarik"
	var anoNascimento = 1995
	var anoAtual = 2025
	#Ajuste o código para levar em consideração se a pessoa já fez aniversário ou não. Se ela não fez aniversário o cálculo da idade deverá ser (anoAtual - anoNascimento - 1), do contrário deverá ser (anoAtual - anoNascimento)
	var fezAniversario = false
	
	var idade
	
	if (fezAniversario == true):
		idade = anoAtual - anoNascimento
	else:
		idade = anoAtual - anoNascimento - 1
	
	print("Olá ",nome,", seja bem vindo! Você tem ",idade," anos de idade!")
