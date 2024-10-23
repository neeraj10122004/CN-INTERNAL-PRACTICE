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
    print("connection : ",address)

    while True :
        data = connection.recv(1024).decode()
        if not data :
            break
        else :
            if random.random()>0.5 :
                t.sleep(3)
                data = "not recived"
                connection.send(data.encode())
            else :
                data = "recived : "+str(data)
                print(data)
                connection.send(data.encode())
    connection.close()

server()