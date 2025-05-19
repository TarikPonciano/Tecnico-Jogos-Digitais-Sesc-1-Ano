extends Node2D

var pontuacao = 0

var poder_clique = 1

var qtd_upgrade_clique = 0
var custo_upgrade_clique = 10

func atualizarInterface():
	$RotuloPontuacao.text = str("Pontuação: ", pontuacao)
	$BotaoClique.text = str("Clique Aqui (+",poder_clique,")")
	$BotaoUpgradeClique.text = str("Upgrade Clique: ", custo_upgrade_clique," pontos")

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
