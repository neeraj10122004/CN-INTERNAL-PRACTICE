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
    print(str(address))

    while True :
        data = connection.recv(1024).decode()
        if not data :
            break
        if random.random()>0.5 :
            t.sleep(5)
            resp="not recived"
            connection.send(resp.encode())
        else:
            print("recived",str(data))
            resp = "recived"+str(data)
            connection.send(resp.encode())
    connection.close()
    
server()


         
        