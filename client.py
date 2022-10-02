from socket import *
HOST = "10.120.70.117"
trackerName = HOST
trackerPort = 6001
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("Input handle:")
#wait for input
#now convert from String to bytes
clientSocket.sendto(message.encode(),(trackerName, trackerPort))
#wait for response from tracker
modifiedMessage, trackerAddress = clientSocket.recvfrom(2048)
#now convert from bytes to string again
print(modifiedMessage.decode())
clientSocket.close()
