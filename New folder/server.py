import socket as s
import time as t
import random

def server():
    host = s.gethostname()
    port = 1234
    server_socket = s.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    connec, address = server_socket.accept()
    print("Connection from : " + str(address))
    while True:
        data = connec.recv(1024).decode()
        if not data:
            break
        if random.random() > 0.5:
            t.sleep(4)
            data = "Not Received"
            connec.send(data.encode())
            continue
        print("Received data: " + str(data))
        response = "Data received: " + str(data)
        connec.send(response.encode())
    connec.close()

server()
