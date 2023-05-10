import socket

c = socket.socket()
c.connect(("localhost", 9999))
print("Connected to the server")

while True:
    # Prompt the user to enter a message to send to the server
    clientMessage = input("Type your message: ")
    
    # Send the message to the server
    c.send(bytes(clientMessage, "utf-8"))
    
    # Check if the user wants to disconnect from the server
    if clientMessage.lower() == "exit":
        break
    
    # Receive the server's response and print it to the console
    serverMessage = c.recv(1024).decode()
    print("Server says:", serverMessage)

print("Disconnected from the server")
c.close()
