extends Node2D

var num1
var num2
var op

func _on_botao_1_pressed() -> void:
	$Label.text += "1"


func _on_botao_2_pressed() -> void:
	$Label.text += "2"


func _on_botao_3_pressed() -> void:
	$Label.text += "3"


func _on_botao_4_pressed() -> void:
	$Label.text += "4"


func _on_botao_5_pressed() -> void:
	$Label.text += "5"


func _on_botao_6_pressed() -> void:
	$Label.text += "6"


func _on_botao_9_pressed() -> void:
	$Label.text += "9"


func _on_botao_7_pressed() -> void:
	$Label.text += "7"


func _on_botao_8_pressed() -> void:
	$Label.text += "8"


func _on_botao_0_pressed() -> void:
	$Label.text += "0"


func _on_botao_adição_pressed() -> void:
	num1 = float($Label.text)
	$Label.text = ""
	op = "+"
	

func _on_botao_calcular_pressed() -> void:
	num2 = float($Label.text)
	
	if op == "+":
		$Label.text = str(num1+num2)
	elif op == "-":
		$Label.text = str(num1-num2)


func _on_botao_subtração_pressed() -> void:
	num1 = float($Label.text)
	$Label.text = ""
	op = "-"
