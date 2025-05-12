extends Node2D

func _on_botao_calcular_pressed() -> void:
	#Coletar informações
	var num1 = float($CampoPrimeiroNumero.text)
	var num2 = float($CampoSegundoNumero.text)
	var op = $ListaOperacoes.get_selected_id()
	#Calcular o resultado dependendo da operação
	
	if (op == 0):
		$RotuloResultado.text = str("Resultado: ", (num1+num2))
	elif (op == 1):
		$RotuloResultado.text = str("Resultado: ", (num1-num2))
	elif (op == 2):
		$RotuloResultado.text = str("Resultado: ", (num1*num2))
	elif (op == 3):
		if num2 == 0:
			$RotuloResultado.text = str("Resultado: TENTATIVA DE DIVISÃO POR ZERO!")
		else:
			$RotuloResultado.text = str("Resultado: ", (num1/num2))
	else:
		$RotuloResultado.text = str("Resultado: OPERAÇÃO NÃO SELECIONADA OU INVÁLIDA!")
	
	
	#Exibir resultado na tela
