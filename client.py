import socket
c = socket.socket()
c.connect(("localhost",9999))
clientMessage = input("Write your message: ")
c.send(bytes(clientMessage , "utf-8"))
msg = c.recv(1024).decode()

print(msg)