extends Node2D

var pontuacao = 0

func _ready() -> void:
	print("PROGRAMA INICIADO")
	var nome = "Tarik"
	print("Hello, ", nome,"!")
	$Label.text = str("Hello, ", nome,"!")

func _process(delta: float) -> void:
	
	if Input.is_action_just_pressed("ui_accept"):
		pontuacao += 1
		$Label2.text = str(pontuacao)
	
