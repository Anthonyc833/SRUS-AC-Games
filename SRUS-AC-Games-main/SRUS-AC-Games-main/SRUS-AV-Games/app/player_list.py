class PlayerList:
    def __init__(self, headPlayer, tail):
        self.headPlayer = headPlayer
        headPlayer = None
        self.tail = tail

    def insertNode(self):
        if self.headPlayer == None:
            return self.headPlayer += self.tail
        
