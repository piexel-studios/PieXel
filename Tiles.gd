extends TileMap

# Declare member variables here. Examples:



# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

func get_tile(tile_name):
	return tile_set.find_tile_by_name(tile_name)

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
