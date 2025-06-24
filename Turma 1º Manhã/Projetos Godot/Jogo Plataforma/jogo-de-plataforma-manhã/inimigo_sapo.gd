extends CharacterBody2D


const SPEED = 200.0
const JUMP_VELOCITY = -400.0
var direction = 0


func _physics_process(delta: float) -> void:
	# Add the gravity.
	if not is_on_floor():
		velocity += get_gravity() * delta


	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions.
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

#Técnica usando o timer
func _on_timer_timeout() -> void:
	var random = RandomNumberGenerator.new()
	var direcoes = [-1,0,1]
	direction = direcoes[random.randi_range(0,2)]
