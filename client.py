from socket import *
import random
HOST = "192.168.1.27"
trackerName = HOST
trackerPort = 6001
clientSocket = socket(AF_INET, SOCK_DGRAM)
listenTest = 0

#-----------CMD List Milestone----------
#1 register (handle) (IP) (port)
#2 query handles
#3 follow jacob jessica
#4 drop jacob jessica

## getting the hostname by socket.gethostname() method
hostname = gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = gethostbyname(hostname)
## getting the PORT number for this host
clientPort = random.randint(6002, 6100)
clientSocket.bind(('0.0.0.0', clientPort))

## printing the hostname and ip_address
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
print(f"Port number: {clientPort}")
initialMessage = "Initial " + str(ip_address) + " " + str(clientPort)
clientSocket.sendto(initialMessage.encode(), (trackerName, trackerPort))
modifiedMessage, trackerAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())

while True:
    #wait for input
    message = input("Input function:")
    #now convert from String to bytes
    clientSocket.sendto(message.encode(),(trackerName, trackerPort))
    #wait for response from tracker
    modifiedMessage, trackerAddress = clientSocket.recvfrom(2048)
    #now convert from bytes to string again
    print(modifiedMessage.decode())
    split_message = modifiedMessage.decode().split(' ')
    #GONNA NEED TO SEND STUFF TO EACH USER THAT TWEETS THIS STUFFERINO USING THE TABLE
    
    if (modifiedMessage.decode() == "exit"):
        print("Graceful deletion complete.")
        clientSocket.close()
        exit()
    
    if (modifiedMessage.decode() == "listen"):
        while listenTest < 1:
            modifiedMessage, trackerAddress = clientSocket.recvfrom(2048)
            listenTest += 1
            print(modifiedMessage.decode())

    if (split_message[0] == "tweet"):
        message = "propagate"
        clientSocket.sendto(message.encode(), (trackerName, trackerPort))
        modifiedMessage, trackerAddress = clientSocket.recvfrom(2048)
        #now convert from bytes to string again
        print(modifiedMessage.decode())


