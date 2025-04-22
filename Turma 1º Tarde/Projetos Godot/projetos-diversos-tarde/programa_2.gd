extends Node2D

func _on_button_pressed() -> void:
	var nome = $LineEdit.text
	
	var idade = int($LineEdit2.text)
	
	$Label2.text = str("Olá, ",nome,"! Seja Bem Vindo!")
	
	if (idade >=18):
		$Label3.text = "RESULTADO: VOCÊ É MAIOR DE IDADE!"
	else:
		$Label3.text = "RESULTADO: VOCÊ É MENOR DE IDADE!"
