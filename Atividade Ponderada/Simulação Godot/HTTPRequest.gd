extends HTTPRequest

#
## Called when the node enters the scene tree for the first time.
#func _ready():
#	self.connect("request_completed", self, "_on_request_completed")		
#	var abc = self.request('http://127.0.0.1:5000/coordenada')		
#	if abc != OK:				
#		push_error("Um erro ocorreu!")
#
#
## Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	var positions = parse_json(body.get_string_from_utf8())		
#	print(positions)
	
	# Function that runs at the beginning of the program, which makes the HTTP request
func _ready():		
	self.connect("request_completed", Callable(self, "_on_request_completed"))		
	var abc = self.request("http://127.0.0.1:5000/godot")		
	if abc != OK:				
		push_error("Um erro ocorreu!")
# If the request is successful, it will show the values ​​read
func _on_request_completed(result, response_code, headers, body):		
	var test_json_conv = JSON.new()
	test_json_conv.parse(body.get_string_from_utf8())		
	var positions = test_json_conv.get_data()
	print(positions)
