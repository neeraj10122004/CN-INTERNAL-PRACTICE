import socket as s
import random
import time as t
def server():
    host = s.gethostname()
    port = 1234
    socket = s.socket()
    socket.bind((host,port))
    socket.listen(2)
    connection,address = socket.accept()
    print("connection : ",str(address))
    while True : 
        data = connection.recv(1024).decode()
        if not data :
            break
        if random.random() > 0.5 :
            t.sleep(4)
            data = "Not Recived"
            connection.send(data.encode())
            continue
        print("data : ",str(data))
        response = "recived"+str(data)
        connection.send(response.encode())
    connection.close()

server()
