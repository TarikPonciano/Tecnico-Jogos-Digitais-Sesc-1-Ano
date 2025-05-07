extends Node2D

func _ready() -> void:
	#Crie um programa que contém o nome e o ano de nascimento de uma pessoa. Calcule e exiba no terminal uma mensagem de boas vindas e a idade dessa pessoa
	var nome = "Gesonel"
	var anoNascimento = 2010
	var anoAtual = 2025
	var fezAniversario = true
	var idade
	
	if (fezAniversario == true):
		idade =  anoAtual - anoNascimento
	else:
		idade =  anoAtual - anoNascimento - 1
	
	print("Seja bem vindo ", nome,"! Você tem ",idade, " anos!")
