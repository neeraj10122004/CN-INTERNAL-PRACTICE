import socket as s

def client():
    host = s.gethostname()
    port = 1234
    socket = s.socket()
    socket.connect((host,port))
    n = int(input("enter nuber of packets"))
    c = 0
    inpstr = "enter packet"
    while c < n :
        data = input(inpstr)
        data=data.encode()
        socket.send(data)
        resp = socket.recv(1024).decode()
        if str(resp)=="not recived" :
            inpstr = "resend the packet"
        else:
            inpstr = "enter packet"
            print("data : ",data)
            c+=1
    socket.close()
client()