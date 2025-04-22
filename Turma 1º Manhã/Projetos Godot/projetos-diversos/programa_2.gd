extends Node2D


func _on_button_pressed() -> void:
	var nome = $LineEdit.text
	var idade = int($LineEdit2.text)
	
	if (idade >= 18):
		$Label2.text = "RESULTADO: Maior de idade!"
	else:
		$Label2.text = "RESULTADO: Menor de idade!"
	
	$Label.text = str("Olá, ",nome,"!")
