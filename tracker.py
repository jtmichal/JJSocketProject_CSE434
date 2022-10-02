from socket import *
HOST = "192.168.1.10"
trackerPort = 6001
trackerSocket = socket(AF_INET, SOCK_DGRAM)
trackerSocket.bind((HOST, trackerPort))
handle_list = []
follower_list = []

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

def getHandles() -> str:
    count = list.len()
    list = handle_list
    ans = ' '.join(list)
    return ans

def follow(follower, followee) -> str:
    for x in follower_list:
        if x == follower:
            print("You're already following this user.")
            info = "Failed"
            return info
    follower_list.append(follower)
    follower_list.sort()
    info = "Success"
    return info

def drop(follower, followee) -> str:
    for x in follower_list:
        if x == follower:
            follower_list.remove(follower)
            info = "Success"
            return info
    print("You don't follow this user")
    info = "Failure"
    return info




print("The server is ready to receive")
while True:
    message, clientAddress = trackerSocket.recvfrom(2048)
    modifiedMessage = register(message, "0.0.0.0", trackerPort)
    trackerSocket.sendto(modifiedMessage.encode(), clientAddress)


 

