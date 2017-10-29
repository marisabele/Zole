import unittest
from zolegame.player import Player
from zolegame.rules import Rules

class PlayerTest(unittest.TestCase):

    class PlayerFirstCard(Player):
        def _getCard(self, requested_suit_card):
            return Rules.allowedCards(requested_suit_card, self.cards)[0]

    def setUp(self):
        self.player = Player("0000", "testPlayer", 100)
    def test_playerInterface(self):
        self.player.newGame();
        self.player.addCards([0,1,2,3,4,5,6,7])
        self.player.updatePoints(2)
        self.assertEqual(None, self.player.selectContract(['t','p']))
        self.assertEqual(None, self.player.selectCard(None))
        self.player.addTrick([0, 1, 2])

    def test_addCards(self):
        cards = tuple(xrange(8))
        self.player.newGame()
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

    def test_cardSelect(self):
        #add cards
        player = self.PlayerFirstCard("0000", "testPlayer", 100)
        player.newGame()
        cardSet = [1, 2, 15, 18, 19]
        player.addCards(cardSet)
        self.assertEqual(len(cardSet), len(player.cards))

        playedCard = player.selectCard(0)
        self.assertEqual(1, playedCard)
        self.assertEqual(len(cardSet)-1, len(player.cards))

        playedCard = player.selectCard(14)
        self.assertEqual(15, playedCard)
        self.assertEqual(len(cardSet)-2, len(player.cards))
