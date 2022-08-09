import unittest
from playerlist import PlayerList

a_HeadPlayer = ""
a_tail = ""
a_key = ""
a_display = True

class testPlayerList(unittest.TestCase):
    def playerListstr(self):
        player_list = PlayerList(a_HeadPlayer, a_tail, a_key)
        self.assertIn(a_HeadPlayer, player_list.__str__())
        self.assertIn(a_tail, player_list.__str__())
        self.assertIn(a_key, player_list.__str__())
        self.assertIn(a_display, player_list.__str__())



def liststr():
    player_list = PlayerList(a_HeadPlayer, a_tail, a_display)
    assert a_HeadPlayer in player_list.__str__()
    assert a_tail in player_list.__str__()
    assert a_key in player_list.__str__()
    assert  a_display in player_list.__str__()
    assert(a_HeadPlayer, a_tail, a_key == tuple(player_list))

