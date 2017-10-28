import unittest
import zolegame.rules as U

class RulesTest(unittest.TestCase):

    def test_ranking_index(self):
        self.assertEqual([0, 14, 18], U.Rules.card_deck_ranking([0, 14, 18]))
        self.assertEqual([14, 18, 22], U.Rules.card_deck_ranking([14, 18, 22]))
        self.assertEqual([14, 18, 22], U.Rules.card_deck_ranking([18, 14, 22]))
        self.assertEqual([14, 18, 22], U.Rules.card_deck_ranking([22, 14, 18]))

    def test_best_card(self):
        self.assertEqual(0, U.Rules.best_card([0, 1, 2]))
        self.assertEqual(1, U.Rules.best_card([1, 0, 2]))
        self.assertEqual(2, U.Rules.best_card([2, 1, 0]))

        self.assertEqual(0, U.Rules.best_card([0, 14, 15]))
        self.assertEqual(1, U.Rules.best_card([14, 0, 15]))
        self.assertEqual(0, U.Rules.best_card([14, 15, 16]))
        self.assertEqual(1, U.Rules.best_card([15, 14, 16]))
        self.assertEqual(0, U.Rules.best_card([14, 18, 22]))
        self.assertEqual(0, U.Rules.best_card([14, 15, 22]))
        self.assertEqual(2, U.Rules.best_card([14, 15, 1]))

        self.assertEqual(0, U.Rules.best_card([18, 19, 20]))
        self.assertEqual(0, U.Rules.best_card([19, 14, 16]))

        self.assertEqual(0, U.Rules.best_card([22, 23, 24]))
        self.assertEqual(0, U.Rules.best_card([25, 14, 16]))

    def test_allowed_cards(self):
        self.assertEqual([1,2], U.Rules.allowed_cards(0, [1, 2, 14]))
        self.assertEqual([1], U.Rules.allowed_cards(0, [1, 22, 14]))
        self.assertEqual([14, 15, 16], U.Rules.allowed_cards(0, [14, 15, 16]))
        self.assertEqual([14, 15, 16], U.Rules.allowed_cards(17, [14, 15, 16]))
        self.assertEqual([18, 22, 23], U.Rules.allowed_cards(14, [18, 22, 23]))
        self.assertEqual([0, 24], U.Rules.allowed_cards(18, [24, 0]))
        self.assertEqual([24], U.Rules.allowed_cards(22, [24, 0]))
