extends CharacterBody2D


const SPEED = 200.0
const JUMP_VELOCITY = -400.0
var direction = -1


func _physics_process(delta: float) -> void:
	# Add the gravity.
	if not is_on_floor():
		velocity += get_gravity() * delta

	velocity.x = SPEED * direction

	move_and_slide()


func _on_timer_timeout() -> void:
	var direcoes = [-1, 0, 1]
	
	var rng = RandomNumberGenerator.new()
	
	direction = direcoes[rng.randi_range(0,2)]
