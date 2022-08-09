from player import Player
class PlayerNode:
    def __init__(self,player, UID, key, next, prev ):
        self.player = player
        self.UID = UID
        self.key = key
        self.next = next
        self.prev = prev
        self.next = None
        self.prev = None

        key = self.UID

    def __str__(self):
        return f"{self.player}, {self.UID}, {self.key}"

    def get_player(self):
        return self.player

    def setName(self, PLayeruser):
        self.player = PLayeruser

    def getUID(self):
        return self.UID

    def setUID(self, UID):
        self.UID = UID

    def getKey(self):
        return self.key

    def setkey(self, keys):
        self.key = keys

    def getnext(self):
        return self.next

    def setnext(self, Next):
        self.next = Next

    def getprev(self):
        return self.prev

    def setprev(self, Prev):
        self.prev = Prev


