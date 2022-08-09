from player import Player
class PlayerList:
    def __init__(self, headPlayer, key):
        self.headPlayer = headPlayer
        self.headPlayer = None
        self.key = key
        self.key = Player(UID="00")

    def is_empty(self):
        return bool(self.head)


    def insertNode(self):
        if self.is_empty():
            self.headPlayer += Player(Player, self.node)


    def insertTail(self):
        if self.tail == None:
            self.tail += Player(Player, self.node)

    def deletefromHead(self):
       self.headPlayer.remove()

    def deletefromTail(self):
        self.tail.remove()

    def removebykey(self):
        self.key.remove()

        
