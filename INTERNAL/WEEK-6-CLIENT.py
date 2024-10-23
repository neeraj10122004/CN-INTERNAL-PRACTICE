import socket as s

def client() :
    host = s.gethostname()
    port = 1234
    socket = s.socket()
    socket.connect((host,port))
    n = int(input("enter number of packets : "))
    inpdata = "enter the packet"
    c=0
    while c < n :
        data = input(inpdata)
        socket.send(data.encode())
        ack = socket.recv(1024).decode()
        if ack == "Not Recived":
            inpdata = "data not recived resend"
        else :
            inpdata = "enter the packet"
            print(ack)
            c +=1
    socket.close()
client()



