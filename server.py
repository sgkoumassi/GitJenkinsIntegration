import socket
import threading

class ThreadForClient(threading.Thread):
	def __init__(self,client):
		threading.Thread.__init__(self)
		self.conn = conn

	def run(self):
		data= self.conn.recv(1024)
		data =data.decode("utf8")
		print(data)



host,port=('',5566)

socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind((host,port))
print("Server started .....")

while True:
	socket.listen(5)
	conn,adress = socket.accept()
	print("Listening ....")
	print("Client connected")

	myThread1 = ThreadForClient(conn)
	myThread2 = ThreadForClient(conn)

	myThread1.start()
	myThread2.start()

	myThread1.join()
	myThread2.join()

	

conn.close()
print ("socket closed !!")
socket.close()
