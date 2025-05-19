extends Node2D

var pontuacao = 0

var poder_clique = 1
var poder_passivo = 0

var qtd_upgrade_clique = 0
var custo_upgrade_clique = 10

var qtd_upgrade_1 = 0
var custo_upgrade_1 = 20

var qtd_upgrade_2 = 0
var custo_upgrade_2 = 100

	
func atualizarInterface():
	$RotuloPontuacao.text = str("Pontuação: ", pontuacao)
	$BotaoClique.text = str("Clique Aqui (+",poder_clique,")")
	$BotaoUpgradeClique.text = str("Upgrade Clique: ", custo_upgrade_clique," pontos")
	$MenuUpgrades/CaixaUpgrade1/ComprarUpgrade1.text = str("Comprar\n",custo_upgrade_1," pontos")
	$MenuUpgrades/CaixaUpgrade2/ComprarUpgrade2.text = str("Comprar\n",custo_upgrade_2," pontos")
	$RotuloPoderPassivo.text = str("P/S: ",poder_passivo, "/s")

func _on_botao_clique_pressed() -> void:
	pontuacao += poder_clique
	atualizarInterface()
	
func _on_botao_upgrade_clique_pressed() -> void:
	if pontuacao >= custo_upgrade_clique:
		poder_clique += 1
		pontuacao -= custo_upgrade_clique
		qtd_upgrade_clique += 1
		custo_upgrade_clique *= 1.2
		custo_upgrade_clique = int(custo_upgrade_clique)
		
		atualizarInterface()


func _on_comprar_upgrade_1_pressed() -> void:
	if pontuacao >= custo_upgrade_1:
		poder_passivo += 1
		pontuacao -= custo_upgrade_1
		qtd_upgrade_1 += 1
		custo_upgrade_1 *= 1.2
		custo_upgrade_1 = int(custo_upgrade_1)
		
		atualizarInterface()


func _on_timer_timeout() -> void:
	pontuacao += poder_passivo
	atualizarInterface()


func _on_comprar_upgrade_2_pressed() -> void:
		if pontuacao >= custo_upgrade_2:
			poder_passivo += 5
			pontuacao -= custo_upgrade_2
			qtd_upgrade_2 += 1
			custo_upgrade_2 *= 1.2
			custo_upgrade_2 = int(custo_upgrade_2)
			
			atualizarInterface()
