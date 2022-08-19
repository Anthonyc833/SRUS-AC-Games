from player import Player
from player_node import PlayerNode
class PlayerList:
    def __init__(self, head_player: Player = None, tail_player: Player = None):
        self._head_player = head_player
        self._tail_player = tail_player

    @property
    def key(self, player):
        return player.get_uid()

    def is_empty(self):
        return bool(self.head)


    def insert_node(self):
        if self.is_empty():
            self._head_player += Player(Player, self.node)


    def insert_tail(self):
        if self._tail_player == None:
            self._tail_player += Player(Player, self.node)

    def delete_from_head(self):
       self._head_player = self._tail_player

    def delete_from_tail(self):
        self.tail == self._head_player

    def remove_by_key(self, next_, prev):
        if PlayerNode == Player.get_uid(self):
            PlayerNode.getnext(self.prev)
            PlayerNode.getprev(self.next_)


    def display(self):
        forward = True
        if self.tail == True:
            forward = False
        else:
            forward = True
            print(self._head_player())


        
