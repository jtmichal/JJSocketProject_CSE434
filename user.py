class User:
    def __init__(self, handle, HOST, trackerPort, followers = []):
        self.handle = handle
        self.HOST = HOST
        self.trackerPort = trackerPort
        self.followers = followers