from socket import *

# Client setup
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    # user choose function
    chosenFunction = input("Choose function (Random, Add, Subtract): ")
    clientSocket.send(chosenFunction.encode()) # send chosen function

    clientSocket.recv(1024).decode() # receive prompt for 'input numbers'
    print("Server:", "Input numbers")
    # user input numbers 
    numbers = input("Input two numbers separated by space: ")
    clientSocket.send(numbers.encode()) # send numbers

    result = clientSocket.recv(1024).decode() # receive result
    print("Server:", result)
