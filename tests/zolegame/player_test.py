import unittest
from zolegame.player import Player

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player("0000", "testPlayer", 100)

    def test_addCards(self):
        cards = tuple(xrange(8))
        self.player.addCards(cards)
        self.assertEqual(cards[0], self.player.cards[0])
        self.assertEqual(8, len(self.player.cards))

    def test_points(self):
        self.assertEqual(100, self.player.points)
        self.player.updatePoints(10)
        self.assertEqual(110, self.player.points)
        self.player.updatePoints(-10)
        self.assertEqual(100, self.player.points)
        self.player.updatePoints(0)
        self.assertEqual(100, self.player.points)

    def test_resp(self):
        self.assertEqual("{'name': 'testPlayer', 'uuid': '0000'}", str(self.player))
