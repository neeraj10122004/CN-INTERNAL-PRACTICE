import socket as s

def client():
    host = s.gethostname()
    port = 1234
    client_socket = s.socket()
    client_socket.connect((host, port))
    n = int(input("Enter Number of Packets : "))
    input_data = "Enter Packet of Data : "
    c = 0
    while c < n:
        datapacket = input(input_data)
        datapacket = str(datapacket)
        client_socket.send(datapacket.encode())
        acknowledgement = client_socket.recv(1024).decode()
        if acknowledgement == "Not Received":
            input_data = "Data not received!! Resend the previous data : "
        else:
            input_data = "Enter Packet of Data : "
            print(acknowledgement)
            c += 1
    client_socket.close()

client()