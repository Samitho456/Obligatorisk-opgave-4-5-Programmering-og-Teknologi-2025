from socket import *
import json

# Client setup
serverName = 'localhost'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

request = {"operation": "", "numbers": []}
while True:
    # user choose function
    chosenFunction = input("Choose function (Random, Add, Subtract): ")
    request["operation"] = chosenFunction

    # user input numbers
    while True:
        try:
            number1 = int(input("Input first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        try:
            number2 = int(input("Input second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    request["numbers"] = [number1, number2]

    clientSocket.send(json.dumps(request).encode()) # send request
    result = json.loads(clientSocket.recv(1024).decode()) # receive result
    print("Server:", result["result"])
