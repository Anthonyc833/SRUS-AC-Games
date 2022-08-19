import unittest

import player
import playerlist
from playerlist import PlayerList
from player_node import PlayerNode
from player import Player

a_display = True

class testPlayerList(unittest.TestCase, PlayerNode, PlayerList ):
    def test_player_list_str(self):
        player_list = PlayerList(self, head_player= None, tail_player=None)


    def test_list_str(self):
        player_list = PlayerList(self, head_player= None)


    def test_list_link(self):
        assert PlayerList(self, tail_player=None)


    def test_removal(self):
        assert PlayerList.delete_from_head(PlayerList(self, tail_player=PlayerNode.setnext(self, Next=None)))

    def test_tail_remove(self):
        assert PlayerList.delete_from_tail(PlayerList(self, head_player = PlayerNode.setprev(self, Prev= None)))

    def test_removal_by_key(self, next_, prev):
        assert PlayerList.remove_by_key(PlayerList(self, next_= prev, prev = next_))

def main():
    testPlayerList()

if __name__ == "__main__":
    main()