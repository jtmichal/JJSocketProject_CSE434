from socket import *
HOST = "10.120.70.145"
serverName = HOST
serverPort = 6001
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("Input lowercase sentence:")
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
