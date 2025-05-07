extends Node2D


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	print("RODANDO!!!")


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass


func _on_button_pressed() -> void:
	var nome = $LineEdit.text
	var anoNascimento = int($LineEdit2.text)
	var anoAtual = int($LineEdit3.text)
	var fezAniversario = $CheckButton.button_pressed
	
	var idade
	
	if (fezAniversario == true):
		idade = anoAtual - anoNascimento
	else:
		idade = anoAtual - anoNascimento - 1
		
	$Label5.text = str("Resultado: ", idade, " anos!")
		
		
