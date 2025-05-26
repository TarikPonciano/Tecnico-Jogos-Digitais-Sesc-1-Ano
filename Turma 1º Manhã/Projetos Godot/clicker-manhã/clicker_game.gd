extends Node2D

var score = 0
var power_click = 1
var custo_upgrade_click = 10
var qtd_upgrade_click = 0

var power_passive = 0

var qtd_ajudante1 = 0
var custo_ajudante1 = 20
var ganho_ajudante1 = 0.5

var qtd_ajudante2 = 0
var custo_ajudante2 = 100
var ganho_ajudante2 = 1

func _process(delta: float) -> void:
	if Input.is_action_just_pressed("ui_accept"):
		_on_botao_clicar_pressed()
	
	if Input.is_action_just_pressed("botao_1"):
		_on_comprar_ajudante_1_pressed()
	
func _on_botao_clicar_pressed() -> void:
	score += power_click
	atualizar_interface()


func _on_botao_upgrade_click_pressed() -> void:
	
	if score >= custo_upgrade_click:
		
		score -= custo_upgrade_click
		custo_upgrade_click *= 1.2
		custo_upgrade_click = int(custo_upgrade_click)
		qtd_upgrade_click += 1
		
		atualizar_ganhos()
		atualizar_interface()


func _on_comprar_ajudante_1_pressed() -> void:
	if score >= custo_ajudante1:
		
		score -= custo_ajudante1
		custo_ajudante1 *= 1.3
		custo_ajudante1 = int(custo_ajudante1)
		qtd_ajudante1 += 1
		
		atualizar_ganhos()
		atualizar_interface()
		


func _on_timer_timeout() -> void:
	score += power_passive
	atualizar_ganhos()
	atualizar_interface()


func _on_comprar_ajudante_2_pressed() -> void:
	if score >= custo_ajudante2:
		
		score -= custo_ajudante2
		custo_ajudante2 *= 1.3
		custo_ajudante2 = int(custo_ajudante2)
		qtd_ajudante2 += 1
		
		atualizar_ganhos()
		atualizar_interface()
		
func atualizar_interface():
	
	$RotuloScore.text = str("Score: ",score,"(+",power_passive,")")
	
	$BotaoUpgradeClick.text = str("Upgrade Click: ",custo_upgrade_click)
	
	$MenuAjudantes/Ajudante1/QuantidadeAjudante1.text = str("QTD\n",qtd_ajudante1)
	$MenuAjudantes/Ajudante1/ComprarAjudante1.text = str("Comprar \n", custo_ajudante1)
	
	$MenuAjudantes/Ajudante2/QuantidadeAjudante2.text = str("QTD\n",qtd_ajudante2)
	$MenuAjudantes/Ajudante2/ComprarAjudante2.text = str("Comprar \n", custo_ajudante2)
	
func atualizar_ganhos():
	power_passive = 0 + (qtd_ajudante1 * ganho_ajudante1) + (qtd_ajudante2 * ganho_ajudante2)
	power_click = 1 + (1*qtd_upgrade_click)
	
