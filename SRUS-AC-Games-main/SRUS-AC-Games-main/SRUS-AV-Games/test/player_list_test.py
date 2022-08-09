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
    player_list = PlayerList(a_HeadPlayer, a_tail, a_name, a_display)
    assert a_HeadPlayer in playerlist.__str__()
    assert a_tail in playerlist.__str__()
    assert a_key in playerlist.__str__()
    assert  a_display in playerlist.__str__()
    assert(a_HeadPlayer, a_tail, a_key == tuple(playerlist))

