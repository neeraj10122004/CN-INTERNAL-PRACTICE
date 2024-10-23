import socket as s

def client():
    host = s.gethostname()
    port = 1234
    socket = s.socket()
    socket.connect((host,port))
    n = int(input("enter the size of data : "))
    inpstr = "enter data"
    c = 0
    while c < n :
        data = input(inpstr)
        socket.send(data.encode())
        ack = socket.recv(1024).decode()
        if ack == "not recived" :
            inpstr = "resend the data"
        else:
            inpstr = "enter next packet"
            print(ack)
            c+=1
    socket.close()

client()
