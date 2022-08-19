from player import Player
class PlayerNode:
    def __init__(self, player: Player, next_=None, prev=None):
        self.player = player
        self.next = next_
        self.prev = prev


    def __str__(self):
        return f"{self.prev}, {self.next}"

    def getnext(self):
        return self.next

    def setnext(self, Next):
        self.next = Next

    def getprev(self):
        return self.prev

    def setprev(self, Prev):
        self.prev = Prev


