from socket import *
import threading
import random

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

# Function to handle client requests
def handleClient(connectionSocket):
    while True:
        message = connectionSocket.recv(1024).decode()
        match message.strip():
            case "Random":
                connectionSocket.send("Input numbers".encode())
                numbers = connectionSocket.recv(1024).decode().split(" ")
                random_number = random.randint(int(numbers[0]), int(numbers[1]))
                connectionSocket.send(str(random_number).encode())
            case "Add":
                connectionSocket.send("Input numbers".encode())
                numbers = connectionSocket.recv(1024).decode().split(" ")
                result = int(numbers[0]) + int(numbers[1])
                connectionSocket.send(str(result).encode())
            case "Subtract":
                connectionSocket.send("Input numbers".encode())
                numbers = connectionSocket.recv(1024).decode().split(" ")
                result = int(numbers[0]) - int(numbers[1])
                connectionSocket.send(str(result).encode())

# Main server loop to accept connections
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(connectionSocket,)).start()