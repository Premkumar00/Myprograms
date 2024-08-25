# Socket program - Server

import threading
import socket

HOST = "192.168.1.47"
PORT = 5213

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

clients = []

print(f"server listening on {HOST}:{PORT}")

def handle_client(client_socket):
	while True:
		message = client_socket.recv(1024).decode()
		if not message:
			break
		else:
			for socket in clients:
				if socket != client_socket:
					socket.send(message.encode())
	client_socket.close()
	clients.remove(client_socket)
	print("Cliemt disconnected")


while True:
	client_socket, address = server_socket.accept()
	print(f"connected: {address}")
	clients.append(client_socket)
	thread = threading.Thread(target=handle_client, args=(client_socket,))
	thread.start()



