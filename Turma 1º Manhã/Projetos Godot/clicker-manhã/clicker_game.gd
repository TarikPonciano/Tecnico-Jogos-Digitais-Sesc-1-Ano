extends Node2D

var score = 0
var power_click = 1
var custo_upgrade_click = 10

func _on_botao_clicar_pressed() -> void:
	score += power_click
	$RotuloScore.text = str("Score: ", score)
	


func _on_botao_upgrade_click_pressed() -> void:
	
	if score >= custo_upgrade_click:
		
		power_click += 1
		score -= custo_upgrade_click
		custo_upgrade_click *= 1.2
		custo_upgrade_click = int(custo_upgrade_click)
		
		$RotuloScore.text = str("Score: ", score)
		$BotaoClicar.text = str("Clique Aqui! (+",power_click,")")
		$BotaoUpgradeClick.text = str("Upgrade Click: ",custo_upgrade_click," points")
