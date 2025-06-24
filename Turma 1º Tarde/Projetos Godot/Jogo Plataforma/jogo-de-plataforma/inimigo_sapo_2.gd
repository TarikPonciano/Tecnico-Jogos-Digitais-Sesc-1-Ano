extends CharacterBody2D


const SPEED = 200.0
const JUMP_VELOCITY = -400.0
var direction = 0
var jogador = null

func _physics_process(delta: float) -> void:
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

	move_and_slide()


func _on_detectar_body_entered(body: Node2D) -> void:
	if body.name == "Jogador":
		jogador = body

func _on_detectar_body_exited(body: Node2D) -> void:
	if body.name == "Jogador":
		jogador = null
