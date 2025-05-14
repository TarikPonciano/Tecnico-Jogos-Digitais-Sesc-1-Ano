extends Node2D

var pontuacao = 0

var poder_click = 1

var custo_upgrade_click = 10
var qtd_upgrade_click = 0

func _on_botao_clique_pressed() -> void:
	pontuacao += poder_click
	
	$RotuloPontuacao.text = str("Pontuação: ", pontuacao)

# Conectar o botão de upgrade ao código
# 1. Verificar se o jogador tem pontuação maior ou igual ao custo do upgrade
# 2. Ao conseguir comprar o upgrade deve aumentar o poder de clique do jogador
# 3. Deve reduzir a pontuação do jogador de acordo com o custo
# 4. Deve elevar o custo para os próximos upgrades
# 5. Atualizar os elementos visuais com as novas informações
#Rotulo -> pontuacao
#BotaoClique -> poder_clique
#BotaoUpgradeClique -> custo_upgrade_clique
func _on_botao_upgrade_clique_pressed() -> void:
	if pontuacao >= custo_upgrade_click:
		
		poder_click += 1
		pontuacao -= custo_upgrade_click
		custo_upgrade_click *= 1.2
		custo_upgrade_click = int(custo_upgrade_click)
		qtd_upgrade_click += 1
		
		$RotuloPontuacao.text = str("Pontuação: ", pontuacao)
		$BotaoClique.text = str("Clique Aqui (+",poder_click,")")
		$BotaoUpgradeClique.text = str("Clique Upgrade: ",custo_upgrade_click," pontos")
