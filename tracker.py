from socket import *
from user import User
HOST = "192.168.1.27"
trackerPort = 6001
trackerSocket = socket(AF_INET, SOCK_DGRAM)
trackerSocket.bind((HOST, trackerPort))
handle_list = []
follower_list = []
split_message = []
full_information = [] #list of tuples sent back from TWEET
clientPorts = []
clientIPs = []
final_message = ''
clientAddresses = []

#Function checks if a handle has been used, checks if it's less than 15 characters, then registers it for use.
def register(handle, IP, clientPort) -> str:
    print("Beginning register(handle, IP, clientPort) process")
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
        user_object = User(username, IP, clientPort, follower_list)
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
    temp_user = []
    for x in list:
        if followee == x.handle:
            for y in x.followers:
                if y == follower:
                    temp_user = x.followers
                    x.followers.remove(follower)
                    x.followers.sort()
                    info = "Success"
                    print(followee + "\'s updated follower list is: " + ' '.join(temp_user))
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

def tweet(handle, message) -> str:
    print("Beginning tweet(handle, message) process")
    if (len(message) <= 140):
        user_follower_list = []
        list = handle_list
        for x in list:
            if handle == x.handle:
                count = len(x.followers)
                user_follower_list = x.followers
                for y in user_follower_list:
                    for z in list:
                        if (y == z.handle):
                            full_information.append([z.handle, z.IP, z.clientPort])
                print("The number of followers " + handle + " currently has is: " + str(count) + "\n" + "The follower list is:\n")
                print(full_information)
                info = "Success"
                print("Ending process")
                return info
    else:
        info = "Failure"
        print("Ending process")
    return info

def end_tweet(handle) -> str:
    info = "Success"
    return info





print("The server is ready to receive")
#permanent while loop until Exit() when a bad input is detected.
while True:
    message, clientAddress = trackerSocket.recvfrom(2048)
    clientAddresses.append(clientAddress)
    split_message = message.decode().split(' ')
    
    if (split_message[0] == "Initial"):
        clientIPs.append(split_message[1])
        clientPorts.append(split_message[2])
        modifiedMessage = "Host detected"
        trackerSocket.sendto(modifiedMessage.encode(), clientAddress)

    elif (split_message[0] == "register"):
        modifiedMessage = register(split_message[1], clientIPs[0], clientPorts[0])
        clientIPs.remove(clientIPs[0])
        clientPorts.remove(clientPorts[0])
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
    
    elif(split_message[0] == "tweet"):
        handle = split_message[1]
        del split_message[0:2]
        final_message = ' '.join(split_message)
        modifiedMessage = tweet(handle, split_message)
        modifiedMessage = "tweet " + modifiedMessage
        trackerSocket.sendto(modifiedMessage.encode(), clientAddress)

        #DO ALL THE LOGICAL RING STUFF
    
    elif(split_message[0] == "propagate"):
        print("Beginning propagation")
        end = end_tweet('jacob')
        modifiedMessage = "Tweet Propagated - " + end
        trackerSocket.sendto(modifiedMessage.encode(), clientAddress)

        
        user_follower_list = []
        list = handle_list
        for x in list:
            if handle == x.handle:
                count = len(x.followers)
                user_follower_list = x.followers
                for y in user_follower_list:
                    for z in list:
                        if (y == z.handle):
                            clientAddress = ('192.168.1.27', int(z.clientPort))
                            index = full_information.index([z.handle, z.IP, z.clientPort])
                            if index == 0:
                                modifiedMessage = "Previous Hop Neighbor: " + x.handle + "\nTweet: " + final_message
                                trackerSocket.sendto(modifiedMessage.encode(), clientAddress)
                            else: 
                                modifiedMessage = "Previous Hop Neighbor: " + user_follower_list[index-1] + "\nTweet: " + final_message
                                trackerSocket.sendto(modifiedMessage.encode(), clientAddress)
                
                print("Ending process")

    elif(split_message[0] == "listen"):
        modifiedMessage = split_message[0]
        trackerSocket.sendto(modifiedMessage.encode(), clientAddress)
    
    elif(split_message[0] == "exit"):
        handle_close = split_message[1]
        for x in handle_list:
            for y in x.followers:
                if handle_close == y:
                    x.followers.remove(handle_close)
            if handle_close == x.handle:
                handle_list.remove(x)
        modifiedMessage = split_message[0]
        trackerSocket.sendto(modifiedMessage.encode(), clientAddress)
        
    else: exit()

    


 

