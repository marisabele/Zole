import unittest
from zolegame.room import Room
from zolegame.player import Player

class RoomTest(unittest.TestCase):
        def setUp(self):
            self.playerA = Player("1", "A", 100)
            self.playerB = Player("2", "B", 100)
            self.playerC = Player("3", "B", 100)
            self.room = Room(['t','d','d'], 10)

        def test_addPlayers(self):
            self.room.addPlayer(self.playerA)
            self.room.addPlayer(self.playerB)
            self.assertEqual(2, len(self.room.players))
            self.room.addPlayer(self.playerC)
            self.assertEqual(3, len(self.room.players))

        def test_nextPlayer(self):
            self.assertEqual(1, self.room.nextPlayer(0))
            self.assertEqual(2, self.room.nextPlayer(1))
            self.assertEqual(0, self.room.nextPlayer(2))
            self.assertEqual(1, self.room.nextPlayer(0))
