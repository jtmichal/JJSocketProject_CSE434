from socket import *
HOST = "general.asu.edu"
serverPort = 6001
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((HOST, serverPort))
print("The server is ready to receive")
while True:
 message, clientAddress = serverSocket.recvfrom(2048)
 modifiedMessage = message.decode().upper()
 serverSocket.sendto(modifiedMessage.encode(),
clientAddress)
