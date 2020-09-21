class Settings:
    def __init__(self):
        self.owner = 134042819152052224
        self.mods = [202447252453588992]
        self.prefix = "!"
        self.decay_time = 5
        self.getToken()
        return
    def getToken(self):
        F = open('token.txt', 'r')
        self.token = F.read()
        F.close()
        return
