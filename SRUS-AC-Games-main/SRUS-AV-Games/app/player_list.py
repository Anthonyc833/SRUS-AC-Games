class PlayerList:
    def __init__(self, headPlayer, tail, key):
        self.headPlayer = headPlayer
        self.tail = tail
        self.key = key

    def insertNode(self):
        if self.headPlayer == None:
            self.headPlayer =+ self.tail

    def insertTail(self):
        if self.tail == None:
            self.tail += self.tail

    def deletefromHead(self):
       self.headPlayer.remove()

    def deletefromTail(self):
        self.tail.remove()

    def removebykey(self):
        self.key.remove()

        
