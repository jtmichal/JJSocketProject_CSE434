from socket import *
from user import User
HOST = "192.168.1.27"
trackerPort = 6001
trackerSocket = socket(AF_INET, SOCK_DGRAM)
trackerSocket.bind((HOST, trackerPort))
handle_list = []
follower_list = []
split_message = []

#Function checks if a handle has been used, checks if it's less than 15 characters, then registers it for use.
def register(handle, HOST, trackerPort) -> str:
    print("Beginning register(handle, HOST, trackerPort) process")
    follower_list = []
    username = handle
    info = "Failed"
    if len(username)<15:
        for x in handle_list:
            if x.handle == username:
                print("This handle is already taken.")
                info = "Failed"
                print("Ending process")
                return info
        user_object = User(username, HOST, trackerPort, follower_list)
        handle_list.append(user_object)
        info = "Success"
        print("Ending process")
        return info
    print("Handle length too long.")
    print("Ending process")
    return info

#Function grabs all handles that have been registered along with the count in a string list object
def getHandles() -> str:
    print("Beginning getHandles() process")
    temp_list = []
    list = handle_list
    for x in list:
        temp_list.append(x.handle)
    count = len(list)
    ans = ' '.join(temp_list)
    returned_str = str(count) + "\n" + ans
    print("Ending process")
    return returned_str

#Function takes the follower and adds it to followee's list of followers if the user exists and if the follower doesn't exist already
def follow(follower, followee) -> str:
    print("Beginning follow(follower, followee) process")
    temp_user = []
    list = handle_list
    for x in list:
        if followee == x.handle:
            for y in x.followers:
                if y == follower:
                    print("You're already following this user.")
                    print("Ending process")
                    info = "Failed"
                    return info
            temp_user = x.followers
            x.followers.append(follower)
            x.followers.sort()
    
    # for x in followee.followers:
    #     if x == follower:
    #         print("You're already following this user.")
    #         print("Ending process")
    #         info = "Failed"
    #         return info
    # followee.followers.append(follower)
    # followee.followers.sort()

    info = "Success"
    print(followee + "\'s updated follower list is: " + ' '.join(temp_user))
    print("Ending process")
    return info

#Function takes follower and removes it from followee's follower list. Only if follower already exists. Opposite of follow.
def drop(follower, followee) -> str:
    print("Beginning drop(follower, followee) process")
    
    list = handle_list
    for x in list:
        if followee == x.handle:
            for y in x.followers:
                if y == follower:
                    x.followers.remove(follower)
                    info = "Success"
                    print("Ending process")
                    return info
    
    
    # for x in follower_list:
    #     if x == follower:
    #         follower_list.remove(follower)
    #         info = "Success"
    #         print("Ending process")
    #         return info

    print("You don't follow this user")
    info = "Failure"
    print("Ending process")
    return info

def tweet(handle) -> str:
    return

def end_tweet(handle) -> str:
    return





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
    
    elif (split_message[0] == "follow"):
        modifiedMessage = follow(split_message[1], split_message[2])
        trackerSocket.sendto(modifiedMessage.encode(), clientAddress)
    
    elif(split_message[0] == "drop"):
        modifiedMessage = drop(split_message[1], split_message[2])
        trackerSocket.sendto(modifiedMessage.encode(), clientAddress)
    
    elif(split_message[0] == "exit"):
        modifiedMessage = split_message[0]
        trackerSocket.sendto(modifiedMessage.encode(), clientAddress)
        
    else: exit()

    


 

