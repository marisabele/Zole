import unittest
from zolegame.players import PlayerInterface

class PlayersTest(unittest.TestCase):

    def setUp(self):
        self.playerAPI = PlayerInterface()

    def test_playersInterface(self):
        self.assertEqual(None, self.playerAPI.receiveMessage("init", ["0","1", 10]))
        self.assertEqual(None, self.playerAPI.receiveMessage("addCards", [0,1, 2]))
        self.assertEqual(None, self.playerAPI.receiveMessage("updatePoints", 5))
        self.assertEqual(None, self.playerAPI.receiveMessage("updatePoints", 5))
        with self.assertRaises(NotImplementedError):
            self.playerAPI.receiveMessage("selectContract", ['t', 'p'])
        self.assertEqual(None, self.playerAPI.receiveMessage("contractSelected", ['12', 'p']))
        with self.assertRaises(NotImplementedError):
            self.playerAPI.receiveMessage("selectCard", [0, 1, 2])
        self.assertEqual(None, self.playerAPI.receiveMessage("cardPlaced", ['12', 1]))
        self.assertEqual(None, self.playerAPI.receiveMessage("trick", ['12', [0]]))
