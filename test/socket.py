# implement a simple client-server socket-based application in Python. 
# write the client program. client should receive the msg from the server and print it on the screen.

# server.py
# import socket
# server_socket = socket.socket()
# server_socked.bind(("127.0.0.1",23000))
# server_socket.listen()
# conn, addr = server_socket.accept()
# msg = "Hello"
# conn.send(msg.encode())
# conn.close()

import socket

server_host = "127.0.0.1"
server_port = 23000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((server_host, server_port))
    
    message = client_socket.recv(1024).decode() 
    
    print("Message from server:", message)
