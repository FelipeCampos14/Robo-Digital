extends Node3D

var URL = "http://127.0.0.1:3000/godot"
var Garra

func _ready():
	Garra = get_node("RigidBody3D")


func _on_button_pressed():
	$CanvasLayer/HTTPRequest.request(URL)
	pass # Replace with function body.


func _on_http_request_request_completed(result, response_code, headers, body):
	var output = body.get_string_from_utf8()
	print("Output: ", output)
	Garra.translate(Vector3(10,10,10))
	pass # Replace with function body.
