import socket

s = socket.socket()
print("Socket has been created")

s.bind(("localhost", 9999))
s.listen(5)
print("Server is waiting for connection")

while True:
    c, addr = s.accept()
    print("Connected with", addr)
    
    while True:
        # Wait for a message from the client
        clientMessage = c.recv(1024).decode()
        print("Received message:", clientMessage)
        
        # Check if the client has disconnected
        if not clientMessage:
            print("Client disconnected")
            break
        
        # Allow the server to input a message to send back to the client
        serverMessage = input("Server message: ")
        
        # Send the server's message to the client
        c.send(bytes(serverMessage, "utf-8"))

    c.close()
