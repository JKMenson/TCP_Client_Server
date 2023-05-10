import socket
s = socket.socket()
print("Socket has been created")
s.bind(("localhost",9999))
s.listen(5)
print("Server is waiting for connection")

while True:
    c, addr = s.accept()
    clientMessage = c.recv(1024).decode()
    print("Connected with", addr, clientMessage)
    c.send(bytes("Welcome to the server", "utf-8"))
    c.close()