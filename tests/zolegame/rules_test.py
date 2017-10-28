import unittest
import zolegame.rules as U

class RulesTest(unittest.TestCase):

    def test_ranking_index(self):
        self.assertEqual([0, 14, 18], U.Rules.cardDeckRanking([0, 14, 18]))
        self.assertEqual([14, 18, 22], U.Rules.cardDeckRanking([14, 18, 22]))
        self.assertEqual([14, 18, 22], U.Rules.cardDeckRanking([18, 14, 22]))
        self.assertEqual([14, 18, 22], U.Rules.cardDeckRanking([22, 14, 18]))

    def test_best_card(self):
        self.assertEqual(0, U.Rules.bestCard([0, 1, 2]))
        self.assertEqual(1, U.Rules.bestCard([1, 0, 2]))
        self.assertEqual(2, U.Rules.bestCard([2, 1, 0]))

        self.assertEqual(0, U.Rules.bestCard([0, 14, 15]))
        self.assertEqual(1, U.Rules.bestCard([14, 0, 15]))
        self.assertEqual(0, U.Rules.bestCard([14, 15, 16]))
        self.assertEqual(1, U.Rules.bestCard([15, 14, 16]))
        self.assertEqual(0, U.Rules.bestCard([14, 18, 22]))
        self.assertEqual(0, U.Rules.bestCard([14, 15, 22]))
        self.assertEqual(2, U.Rules.bestCard([14, 15, 1]))

        self.assertEqual(0, U.Rules.bestCard([18, 19, 20]))
        self.assertEqual(0, U.Rules.bestCard([19, 14, 16]))

        self.assertEqual(0, U.Rules.bestCard([22, 23, 24]))
        self.assertEqual(0, U.Rules.bestCard([25, 14, 16]))

    def test_allowed_cards(self):
        self.assertEqual([1,2], U.Rules.allowedCards(0, [1, 2, 14]))
        self.assertEqual([1], U.Rules.allowedCards(0, [1, 22, 14]))
        self.assertEqual([14, 15, 16], U.Rules.allowedCards(0, [14, 15, 16]))
        self.assertEqual([14, 15, 16], U.Rules.allowedCards(17, [14, 15, 16]))
        self.assertEqual([18, 22, 23], U.Rules.allowedCards(14, [18, 22, 23]))
        self.assertEqual([0, 24], U.Rules.allowedCards(18, [24, 0]))
        self.assertEqual([24], U.Rules.allowedCards(22, [24, 0]))

    def test_nextPlayer(self):
        self.assertEqual(1, U.Rules.nextPlayer(0))
        self.assertEqual(2, U.Rules.nextPlayer(1))
        self.assertEqual(0, U.Rules.nextPlayer(2))
        self.assertEqual(1, U.Rules.nextPlayer(0))
