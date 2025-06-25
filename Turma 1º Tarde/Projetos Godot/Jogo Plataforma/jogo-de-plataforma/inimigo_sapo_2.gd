extends CharacterBody2D


const SPEED = 200.0
const JUMP_VELOCITY = -400.0
var direction = 0
var jogador = null
var morrendo = false

func _physics_process(delta: float) -> void:
	if morrendo:
		return
	# Add the gravity.
	if not is_on_floor():
		velocity += get_gravity() * delta
		
	if jogador == null:
		direction = 0
	elif jogador.position.x > position.x:
		direction = 1
	elif jogador.position.x < position.x:
		direction = -1
	else:
		direction = 0

	velocity.x = SPEED * direction
	
	if velocity.x != 0:
		$AnimatedSprite2D.play("jump")
	else:
		$AnimatedSprite2D.play("idle")
		
	if velocity.x > 0:
		$AnimatedSprite2D.flip_h = true
	elif velocity.x < 0:
		$AnimatedSprite2D.flip_h = false

	move_and_slide()

func morrer():
	$AnimatedSprite2D.play("death")
	morrendo = true
	$CollisionShape2D.disabled = true
	$Hitbox.queue_free()
	await $AnimatedSprite2D.animation_finished
	queue_free()

func _on_detectar_body_entered(body: Node2D) -> void:
	if body.name == "Jogador":
		jogador = body

func _on_detectar_body_exited(body: Node2D) -> void:
	if body.name == "Jogador":
		jogador = null


func _on_hitbox_area_entered(area: Area2D) -> void:
	var alvo = area.get_parent()
	
	if alvo and alvo.name == "Jogador":
		
		if area.name == "Hitbox":
			alvo.morrer()
		elif area.name == "Killzone":
			alvo.velocity.y = -300
			morrer()
		
	
