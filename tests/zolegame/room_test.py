import unittest
from zolegame.room import Room
from zolegame.player import Player
from bots.random_player import RandomPlayer
from zolegame.players import PlayerInterface

class RoomTest(unittest.TestCase):
        def setUp(self):
            self.playerA = PlayerInterface()
            self.playerB = PlayerInterface()
            self.playerC = PlayerInterface()
            self.room = Room(['t','d','d'], 10)

        def test_addPlayers(self):
            self.room.addPlayer(self.playerA)
            self.room.addPlayer(self.playerB)
            self.assertEqual(2, len(self.room.players))
            self.room.addPlayer(self.playerC)
            self.assertEqual(3, len(self.room.players))

        def test_testPlay(self):
            playerA = RandomPlayer()
            playerB = RandomPlayer()
            playerC = RandomPlayer()
            self.room.addPlayer(playerA)
            self.room.addPlayer(playerB)
            self.room.addPlayer(playerC)
            self.room.play()
