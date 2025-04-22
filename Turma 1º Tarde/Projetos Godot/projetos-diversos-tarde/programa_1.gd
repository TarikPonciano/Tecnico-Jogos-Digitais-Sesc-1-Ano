extends Node2D

func _ready() -> void:
	print("Hello World")
	print("Bem vindo ao Godot")
	
	var nome = "Zeca"
	$Label.text = str("Olá, ",nome,"!")
	



#func _process(delta: float) -> void:
	#print("PROGRAMA EXECUTANDO")
