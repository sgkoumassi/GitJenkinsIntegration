import socket

host,port = ('localhost',5566)
socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	socket.connect((host,port))
	print("Client started ....connecttion to server {}".format(port))
	
	data = "Hey my name is Souleymane !! -:)"
	data = data.encode("utf8")
	socket.sendall(data)

except ConnectionRefusedError:
	print("connecttion to server lost ....!!")
finally:
	print ("socket closed !!")
	socket.close()
