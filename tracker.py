from socket import *
HOST = "10.120.70.117"
trackerPort = 6001
trackerSocket = socket(AF_INET, SOCK_DGRAM)
trackerSocket.bind(("0.0.0.0", trackerPort))
handle_list = []

def capitalize(msg):
    cap_msg = msg.decode().upper()
    return cap_msg

def register(handle, HOST, trackerPort) -> str:
    msg = handle.decode()
    info = None
    if len(msg)<15:
        for x in handle_list:
            if x == msg:
                print("This handle is already taken.")
                info = "Failed"
                return info
        handle_list.append(msg)
        info = "Success"
        return info


print("The server is ready to receive")
while True:
 message, clientAddress = trackerSocket.recvfrom(2048)
 modifiedMessage = register(message, "0.0.0.0", trackerPort)
 trackerSocket.sendto(modifiedMessage.encode(), clientAddress)

