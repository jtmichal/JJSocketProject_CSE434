from socket import *
HOST = "192.168.1.10"
trackerPort = 6001
trackerSocket = socket(AF_INET, SOCK_DGRAM)
trackerSocket.bind((HOST, trackerPort))
handle_list = []
follower_list = []
split_message = []

#Function checks if a handle has been used, checks if it's less than 15 characters, then registers it for use.
def register(handle, HOST, trackerPort) -> str:
    msg = handle
    info = None
    if len(msg)<15:
        for x in handle_list:
            if x[0] == msg[0]:
                print("This handle is already taken.")
                info = "Failed"
                return info
        handle_list.append((msg, HOST, trackerPort))
        info = "Success"
        return info

#Function grabs all handles that have been registered along with the count in a string list object
def getHandles() -> str:
    temp_list = []
    list = handle_list
    for x in list:
        temp_list.append(x[0])
    count = len(list)
    ans = ' '.join(temp_list)
    returned_str = str(count) + "\n" + ans
    return returned_str

#Function takes the follower and adds it to followee's list of followers if the user exists and if the follower doesn't exist already
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

#Function takes follower and removes it from followee's follower list. Only if follower already exists. Opposite of follow.
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
#permanent while loop until Exit() when a bad input is detected.
while True:
    message, clientAddress = trackerSocket.recvfrom(2048)
    split_message = message.decode().split(' ')
    
    if (split_message[0] == "register"):
        modifiedMessage = register(split_message[1], "0.0.0.0", trackerPort)
        trackerSocket.sendto(modifiedMessage.encode(), clientAddress)
    
    elif (split_message[0] == "query"):
        modifiedMessage = getHandles()
        trackerSocket.sendto(modifiedMessage.encode(), clientAddress)
        
    else: exit()

    


 

