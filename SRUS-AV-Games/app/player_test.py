import unittest
from player import Player

a_uid = "321"
a_name = "Tony"

class TestPlayer(unittest.TestCase):
    def test_str(self):
        player = Player(a_uid, a_name)
        self.assertIn(a_uid, str(player))
        self.assertIn(a_name, str(player))





def test_str_py():
    player = Player(a_uid, a_name)
    assert a_uid in player.__str__()
    assert a_name in player.__str__()
    assert(a_uid,a_name == tuple(player))


