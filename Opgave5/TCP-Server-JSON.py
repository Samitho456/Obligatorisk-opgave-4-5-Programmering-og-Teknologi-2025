from socket import *
import threading
import random
import json

serverPort = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

# Function to handle client requests
def handleClient(connectionSocket):
    while True:
        message = connectionSocket.recv(1024).decode()

        # Check if message is valid JSON
        try:
            message = json.loads(message)
        except json.JSONDecodeError:
            connectionSocket.send(json.dumps({"error": "Invalid JSON"}).encode())
            continue
        
        # Check if numbers are valid integers
        numbers = message["numbers"]
        for num in numbers:
            if not isinstance(num, int):
                connectionSocket.send(json.dumps({"result": "All values must be integers"}).encode())
                continue
        
        # Perform operation based on the "operation" field
        match message["operation"]:
            case "Random":
                if(numbers[0] > numbers[1]):
                    connectionSocket.send(json.dumps({"result": "First number must be less than second number"}).encode())
                    continue
                random_number = random.randint(int(numbers[0]), int(numbers[1]))
                connectionSocket.send(json.dumps({"result": random_number}).encode())
            case "Add":
                result = int(numbers[0]) + int(numbers[1])
                connectionSocket.send(json.dumps({"result": result}).encode())
            case "Subtract":
                result = int(numbers[0]) - int(numbers[1])
                connectionSocket.send(json.dumps({"result": result}).encode())
            case _:
                connectionSocket.send(json.dumps({"result": "Unknown operation"}).encode())

# Main server loop to accept connections
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(connectionSocket,)).start()