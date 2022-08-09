import unittest
from player import Player

a_uid = "321"
a_name = "Tony"

class TestPlayer(unittest.TestCase):
    def teststr(self):
        player = Player(a_uid, a_name)
        self.assertIn(a_uid, player.__str__())
        self.assertIn(a_name, player.__str__())





def teststr_py():
    player = Player(a_uid, a_name)
    assert a_uid in player.__str__()
    assert a_name in player.__str__()
    assert(_UID,_Name == tuple(player))


