import unittest
#from unittest.mock import patch
from zolegame.game import BaseGame
from zolegame.player import Player
from zolegame.rules import Rules

class BaseGameTest(unittest.TestCase):
        class PlayerGreat(Player):
            def selectContract(self, contract_types):
                return 't'
            def _getCard(self, requested_suit_card):
                return self.cards[0]

        class PlayerSmall(Player):
            def selectContract(self, contract_types):
                return 's'

        class PlayerPartner(Player):
            def selectContract(self, contract_types):
                return 'p'
        class PlayerBig(Player):
            def selectContract(self, contract_types):
                return 'b'

        class PlayerRandom(Player):
            def selectContract(self, contract_types):
                return 't'
            def _getCard(self, requested_suit_card):
                return Rules.allowedCards(requested_suit_card, self.cards)[0]

        class PlayerFirst(Player):
            def selectContract(self, contract_types):
                return 't'
            def _getCard(self, requested_suit_card):
                return self.cards[0]

        def setUp(self):
            self.game = BaseGame(['t','d','b','p','s'], 10)
            self.playerA = Player("abcd", "A", 100)
            self.playerB = Player("ffff", "B", 100)
            self.playerC = Player("0300", "C", 100)

            self.player_great = self.PlayerGreat("01", "Great", 100)
            self.player_partner = self.PlayerPartner("02", "Partner", 100)
            self.player_big = self.PlayerBig("03", "Big", 100)
            self.player_small = self.PlayerSmall("04", "Small", 100)

        def test_addPlayers(self):
            self.game.addPlayers(self.playerA, self.playerB, self.playerC)
            self.assertEqual(self.playerA, self.game.players[0])
            self.assertEqual(self.playerB, self.game.players[1])
            self.assertEqual(self.playerC, self.game.players[2])

        def test_cardDeal(self):
            self.game.addPlayers(self.playerA, self.playerB, self.playerC)
            self.game._dealCards()
            self.assertEqual(8, len(self.game.players[0].cards))
            self.assertEqual(8, len(self.game.players[1].cards))
            self.assertEqual(8, len(self.game.players[2].cards))
            self.assertEqual(2, len(self.game.table_cards))

            self.assertNotEqual([0,1,2,3,4,5,6], len(self.game.players[0].cards))

        def  test_selectContractFirst(self):
             self.game.addPlayers(self.player_great, self.player_great, self.player_great)
             self.game._dealCards()
             self.game._selectContract()
             self.assertEqual('t', self.game.selected_game)

        def  test_selectContractSecond(self):
             self.game.addPlayers(self.player_partner, self.player_great, self.player_great)
             self.game._dealCards()
             self.game._selectContract()
             self.assertEqual('t', self.game.selected_game)

        def  test_selectContractLast(self):
             self.game.addPlayers(self.player_partner, self.player_partner, self.player_great)
             self.game._dealCards()
             self.game._selectContract()
             self.assertEqual('t', self.game.selected_game)

        def  test_selectContractTable(self):
             self.game.addPlayers(self.player_partner, self.player_partner, self.player_partner)
             self.game._selectContract()
             self.assertEqual('d', self.game.selected_game)

        def  test_selectContractBig(self):
             self.game.addPlayers(self.player_partner, self.player_partner, self.player_big)
             self.game._selectContract()
             self.assertEqual('b', self.game.selected_game)

        def  test_selectContractSmall(self):
             self.game.addPlayers(self.player_partner, self.player_partner, self.player_small)
             self.game._selectContract()
             self.assertEqual('s', self.game.selected_game)

        def  test_selectContractNone(self):
             self.game.addPlayers(self.player_partner, self.player_partner, self.player_partner)
             self.game.game_types = ['t','p']
             self.game._selectContract()
             self.assertEqual('p', self.game.selected_game)

        def test_cardDigg(self):
            self.game.addPlayers(self.player_great, self.player_partner, self.player_small)
            self.game._dealCards()
            self.game._selectContract()
            self.assertEqual(2, len(self.game.tricks['01']))

        def test_cardDigg(self):
            self.game.addPlayers(self.player_big, self.player_partner, self.player_small)
            self.game._dealCards()
            self.game._selectContract()
            self.assertEqual(0, len(self.game.tricks['03']))

        def test_payAllCardsTableGame(self):
            player01 = self.PlayerRandom("01", "player01", 100)
            player02 = self.PlayerRandom("02", "player02", 100)
            player03 = self.PlayerRandom("03", "player03", 100)

            self.game.addPlayers(player01, player02, player03)
            self.game._dealCards()
            self.game._selectContract()
            self.game._playTricks()

            self.assertEqual(0, len(self.game.players[0].cards))
            self.assertEqual(0, len(self.game.players[1].cards))
            self.assertEqual(0, len(self.game.players[2].cards))
            self.assertEqual(10, len(self.game.tricks['01'])+
                                len(self.game.tricks['02'])+
                                len(self.game.tricks['03']))

        def test_playNextPlayer(self):
            player01 = self.PlayerFirst("01", "player01", 100)
            player02 = self.PlayerFirst("02", "player02", 100)
            player03 = self.PlayerFirst("03", "player03", 100)
            self.game.addPlayers(player01, player02, player03)

            player01.cards=[25, 18, 4,9]
            player02.cards=[2,21]
            player03.cards=[7,19]
            self.game._selectContract()
            self.game._playTricks()
            self.assertEqual([[25], [18], [21, 19, 9]], self.game.tricks['01'])
            self.assertEqual([[4, 2, 7]], self.game.tricks['02'])
