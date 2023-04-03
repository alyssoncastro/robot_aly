extends Spatial

var hand_offset = Vector3(0, 0, 0) # Define o offset inicial como (0,0,0)

func _ready():
	pass

func _process(delta):
	var input_vector = Vector3(
		Input.get_action_strength("ui_right") - Input.get_action_strength("ui_left"),
		Input.get_action_strength("ui_down") - Input.get_action_strength("ui_up"),
		0
	)
	hand_offset += input_vector * delta * 5 # Ajuste a velocidade de deslocamento (atualmente 5)
	$hand_deslocamento.transform.origin = $eixo_rotacao.transform.origin + hand_offset
