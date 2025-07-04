extends CharacterBody2D


const SPEED = 300.0
const JUMP_VELOCITY = -400.0
var morrendo = false
var cerejas = 0



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
	
	
	if velocity.y < 0:
		$AnimatedSprite2D.play("jump")
	elif velocity.y > 0:
		$AnimatedSprite2D.play("fall")
	elif velocity.x != 0:
		$AnimatedSprite2D.play("correr")
	else:
		$AnimatedSprite2D.play("idle")
	
	if (velocity.x > 0):
		$AnimatedSprite2D.flip_h = false
	elif velocity.x < 0:
		$AnimatedSprite2D.flip_h = true

	move_and_slide()
	
func morrer():
	$AnimatedSprite2D.play("death")
	morrendo = true
	$CollisionShape2D.disabled = true
	$Killzone.queue_free()
	$Hitbox.queue_free()
	await $AnimatedSprite2D.animation_finished
	get_tree().reload_current_scene()
