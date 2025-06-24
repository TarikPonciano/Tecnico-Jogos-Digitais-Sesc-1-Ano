extends CharacterBody2D


const SPEED = 300.0
const JUMP_VELOCITY = -400.0
var morrendo = false

func _physics_process(delta: float) -> void:
	
	if morrendo:
		return
	
	
	# Add the gravity.
	if not is_on_floor():
		velocity += get_gravity() * delta

	# Handle jump.
	if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		velocity.y = JUMP_VELOCITY

	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions.
	var direction := Input.get_axis("ui_left", "ui_right")
	if direction:
		velocity.x = direction * SPEED
		
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)
		
	if velocity.y > 0:
		$AnimatedSprite2D.play("fall")
	elif velocity.y < 0:
		$AnimatedSprite2D.play("jump")
	elif velocity.x != 0:
		$AnimatedSprite2D.play("run")
	else:
		$AnimatedSprite2D.play("idle")
		
	if velocity.x > 0:
		$AnimatedSprite2D.flip_h = false
	elif velocity.x < 0:
		$AnimatedSprite2D.flip_h = true
		

	move_and_slide()
	
func morrer():
	#Para desligar as colisões
	#$"Killzone Jogador".queue_free()
	#$"Hitbox Jogador".queue_free()
	#$CollisionShape2D.queue_free()
	morrendo = true
	$AnimatedSprite2D.play("death")
	await $AnimatedSprite2D.animation_finished
	get_tree().reload_current_scene()
