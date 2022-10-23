class User:
    def __init__(self, handle, IP, clientPort, followers = []):
        self.handle = handle
        self.IP = IP
        self.clientPort = clientPort
        self.followers = followers