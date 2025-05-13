extends Panel

var num1 = 0
var num2 = 0
var op = ""

func _on_botao_1_pressed() -> void:
	$Visor/TextoVisor.text += "1"


func _on_botao_2_pressed() -> void:
	$Visor/TextoVisor.text += "2"

func _on_botao_3_pressed() -> void:
	$Visor/TextoVisor.text += "3"
	
func _on_botao_4_pressed() -> void:
	$Visor/TextoVisor.text += "4"

func _on_botao_5_pressed() -> void:
	$Visor/TextoVisor.text += "5"
	
func _on_botao_6_pressed() -> void:
	$Visor/TextoVisor.text += "6"
	
func _on_botao_7_pressed() -> void:
	$Visor/TextoVisor.text += "7"
	
func _on_botao_8_pressed() -> void:
	$Visor/TextoVisor.text += "8"
	
func _on_botao_9_pressed() -> void:
	$Visor/TextoVisor.text += "9"
	
func _on_botao_0_pressed() -> void:
	$Visor/TextoVisor.text += "0"


func _on_botao_soma_pressed() -> void:
	num1 = float($Visor/TextoVisor.text)
	op = "+"
	
	$Visor/TextoVisor.text = ""
	
func _on_botao_subtracao_pressed() -> void:
	num1 = float($Visor/TextoVisor.text)
	op = "-"
	
	$Visor/TextoVisor.text = ""

func _on_botao_multiplicacao_pressed() -> void:
	num1 = float($Visor/TextoVisor.text)
	op = "*"
	
	$Visor/TextoVisor.text = ""
	
func _on_botao_divisao_pressed() -> void:
	num1 = float($Visor/TextoVisor.text)
	op = "/"
	
	$Visor/TextoVisor.text = ""

func _on_botao_calcular_pressed() -> void:
	num2 = float($Visor/TextoVisor.text)
	
	if (op == "+"):
		$Visor/TextoVisor.text = str(num1+num2)
	elif (op == "-"):
		$Visor/TextoVisor.text = str(num1-num2)
	elif (op == "*"):
		$Visor/TextoVisor.text = str(num1*num2)
	elif (op == "/"):
		$Visor/TextoVisor.text = str(num1/num2)
	else:
		$Visor/TextoVisor.text = str(0)


func _on_botao_ce_pressed() -> void:
	num1 = 0
	num2 = 0
	op = ""
	$Visor/TextoVisor.text = ""
