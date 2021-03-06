import unittest
#from unittest.mock import patch
from zolegame.game import BaseGame
from zolegame.player import Player
from zolegame.rules import Rules
from zolegame.constansts import *

class BaseGameTest(unittest.TestCase):
        class PlayerGreat(Player):
            def _getContract(self, contract_types):
                return 't'
            def _getCard(self, requested_suit_card):
                return self.cards[0]

        class PlayerSmall(Player):
            def _getContract(self, contract_types):
                return 's'

        class PlayerPartner(Player):
            def _getContract(self, contract_types):
                return 'p'
        class PlayerBig(Player):
            def _getContract(self, contract_types):
                return 'b'

        class PlayerRandom(Player):
            def _getContract(self, contract_types):
                return 't'
            def _getCard(self, requested_suit_card):
                return Rules.allowedCards(requested_suit_card, self.cards)[0]

        class PlayerFirst(Player):
            def _getContract(self, contract_types):
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
            self.game.initNewGame()
            self.game._dealCards()
            self.assertEqual(8, len(self.game.players[0].cards))
            self.assertEqual(8, len(self.game.players[1].cards))
            self.assertEqual(8, len(self.game.players[2].cards))
            self.assertEqual(2, len(self.game.table_cards))

            self.assertNotEqual([0,1,2,3,4,5,6], len(self.game.players[0].cards))

        def  test_selectContractFirst(self):
             self.game.addPlayers(self.player_great, self.player_great, self.player_great)
             self.game.initNewGame()
             self.game._dealCards()
             self.game._selectContract()
             self.assertEqual('t', self.game.selected_game)

        def  test_selectContractSecond(self):
             self.game.addPlayers(self.player_partner, self.player_great, self.player_great)
             self.game.initNewGame()
             self.game._dealCards()
             self.game._selectContract()
             self.assertEqual('t', self.game.selected_game)

        def  test_selectContractLast(self):
             self.game.addPlayers(self.player_partner, self.player_partner, self.player_great)
             self.game.initNewGame()
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
            self.game.initNewGame()
            self.game._dealCards()
            self.game._selectContract()
            self.assertEqual(0, len(self.player_big.tricks))

        def test_payAllCardsTableGame(self):
            player01 = self.PlayerRandom("01", "player01", 100)
            player02 = self.PlayerRandom("02", "player02", 100)
            player03 = self.PlayerRandom("03", "player03", 100)

            self.game.addPlayers(player01, player02, player03)
            self.game.initNewGame()
            self.game._dealCards()
            self.game._selectContract()
            self.game._playTricks()

            self.assertEqual(0, len(self.game.players[0].cards))
            self.assertEqual(0, len(self.game.players[1].cards))
            self.assertEqual(0, len(self.game.players[2].cards))
            self.assertEqual(10, len(player01.tricks)+
                                len(player02.tricks)+
                                len(player03.tricks))

        def test_playNextPlayer(self):
            player01 = self.PlayerFirst("01", "player01", 100)
            player02 = self.PlayerFirst("02", "player02", 100)
            player03 = self.PlayerFirst("03", "player03", 100)
            self.game.addPlayers(player01, player02, player03)
            self.game.initNewGame()
            player02.contract = Contract.PARTNER
            player03.contract = Contract.PARTNER
            player01.cards=[25, 18, 4,9]
            player02.cards=[2,21]
            player03.cards=[7,19]
            self.game._selectContract()
            self.game._playTricks()
            self.assertEqual([[25], [18], [21, 19, 9]], player01.tricks)
            self.assertEqual([[4, 2, 7]], player02.tricks)

        def test_playLooseSmallGame(self):
            player01 = self.PlayerFirst("01", "player01", 100)
            player02 = self.PlayerFirst("02", "player02", 100)
            player03 = self.PlayerFirst("03", "player03", 100)
            self.game.addPlayers(player01, player02, player03)
            self.game.initNewGame()
            player01.cards=[15,16,2, 5, 10]
            player02.cards=[1, 6, 12]
            player03.cards=[0, 7, 13]

            self.game._selectContract()
            player01.contract = Contract.SMALL
            self.game.selected_game = Contract.SMALL

            self.game._playTricks()
            self.assertEqual([[15],[16],[7, 5, 6]], player01.tricks)
            self.assertEqual([[2,1,0]], player03.tricks)

        def test_countGamePointsTable(self):
            #_countGamePoints(self, card_points, trick_counts):
            player01 = self.PlayerFirst("01", "player01", 100)
            player02 = self.PlayerFirst("02", "player02", 100)
            player03 = self.PlayerFirst("03", "player03", 100)
            self.game.addPlayers(player01, player02, player03)
            self.game.initNewGame()
            self.game._dealCards()
            self.game._selectContract()

            points = self.game._countGamePoints([120, 0, 0], [8,0,0])
            self.assertEqual(6, points[0])
            self.assertEqual(-3, points[1])
            self.assertEqual(-3, points[2])

            points = self.game._countGamePoints([60, 0, 60], [5,4,1])
            self.assertEqual(-4, points[0])
            self.assertEqual(2, points[1])
            self.assertEqual(2, points[2])

        def test_countGamePointsBig(self):
            player01 = self.PlayerFirst("01", "player01", 100)
            player02 = self.PlayerFirst("02", "player02", 100)
            player03 = self.PlayerFirst("03", "player03", 100)
            self.game.addPlayers(player01, player02, player03)
            self.game.initNewGame()
            self.game._dealCards()
            self.game._selectContract()

            player01.contract = Contract.BIG
            self.game.selected_game = Contract.BIG

            points = self.game._countGamePoints([120, 0, 0], [8,0,0])
            self.assertEqual(14, points[0])
            self.assertEqual(-7, points[1])
            self.assertEqual(-7, points[2])

            points = self.game._countGamePoints([60, 0, 60], [5,4,1])
            self.assertEqual(-12, points[0])
            self.assertEqual(6, points[1])
            self.assertEqual(6, points[2])

        def test_countGamePointsSmall(self):
            player01 = self.PlayerFirst("01", "player01", 100)
            player02 = self.PlayerFirst("02", "player02", 100)
            player03 = self.PlayerFirst("03", "player03", 100)
            self.game.addPlayers(player01, player02, player03)
            self.game.initNewGame()
            self.game._dealCards()
            self.game._selectContract()

            player01.contract = Contract.SMALL
            self.game.selected_game = Contract.SMALL

            points = self.game._countGamePoints([0, 120, 0], [0,8,0])
            self.assertEqual(12, points[0])
            self.assertEqual(-6, points[1])
            self.assertEqual(-6, points[2])

            points = self.game._countGamePoints([60, 0, 60], [5,4,1])
            self.assertEqual(-14, points[0])
            self.assertEqual(7, points[1])
            self.assertEqual(7, points[2])

        def test_countGamePointsDesk(self):
            player01 = self.PlayerFirst("01", "player01", 100)
            player02 = self.PlayerFirst("02", "player02", 100)
            player03 = self.PlayerFirst("03", "player03", 100)
            self.game.addPlayers(player01, player02, player03)
            self.game.initNewGame()
            self.game._dealCards()
            self.game._selectContract()

            player01.contract = Contract.PARTNER
            self.game.selected_game = Contract.DESK

            points = self.game._countGamePoints([0, 120, 0], [0,8,0])
            self.assertEqual(2, points[0])
            self.assertEqual(-4, points[1])
            self.assertEqual(2, points[2])

            points = self.game._countGamePoints([59, 0, 61], [4,0,4])
            self.assertEqual(2, points[0])
            self.assertEqual(2, points[1])
            self.assertEqual(-4, points[2])

        def test_countPonts(self):
            player01 = self.PlayerFirst("01", "player01", 100)
            player02 = self.PlayerFirst("02", "player02", 100)
            player03 = self.PlayerFirst("03", "player03", 100)
            self.game.addPlayers(player01, player02, player03)
            self.game.initNewGame()
            player01.tricks = [[0,1,2],[3]]
            player02.tricks = [[0,1],[3]]
            player03.tricks = [[0],[3]]

            card_points, trick_count = self.game._countPoints()
            self.assertEqual(12, card_points[0])
            self.assertEqual(9, card_points[1])
            self.assertEqual(6, card_points[2])
            self.assertEqual(2, trick_count[0])

        def test_playGame(self):
            player01 = self.PlayerRandom("01", "player01", 100)
            player02 = self.PlayerRandom("02", "player02", 100)
            player03 = self.PlayerRandom("03", "player03", 100)
            self.game.addPlayers(player01, player02, player03)
            self.game.play()
            self.assertTrue(self.game.players[0].points != 100)
            self.assertTrue(self.game.players[1].points != 100)
            self.assertTrue(self.game.players[2].points != 100)

        def test_playerCommunication(self):
            class PlayerComm(Player):
                def sendToClient(self, message, data):
                    self.message = message
                    self.data = data

            player01 = PlayerComm("01", "player01", 100, None, self.game)
            player02 = PlayerComm("02", "player02", 100, None, self.game)
            player03 = PlayerComm("03", "player03", 100, None, self.game)
            self.game.addPlayers(player01, player02, player03)
            #send to all
            self.game.sendToPlayers(None, "testsMsg", [0,0,0])
            self.assertEqual("testsMsg", player01.message)
            self.assertEqual("testsMsg", player02.message)
            self.assertEqual("testsMsg", player03.message)
            self.assertEqual( [0,0,0], player01.data)

            #send to all excet one
            self.game.sendToPlayers("02", "newMessage", [1,2,3])
            self.assertEqual("newMessage", player01.message)
            self.assertEqual("testsMsg", player02.message)
            self.assertEqual("newMessage", player03.message)
            self.assertEqual( [1,2,3], player03.data)

            #player send to public except self
            self.game.sendToPlayers("02", "newMessage", [1,2,3])
            player02._sendToPublic("playerMessage",[4])
            self.assertEqual("playerMessage", player01.message)
            self.assertEqual("testsMsg", player02.message)
            self.assertEqual("playerMessage", player03.message)
            self.assertEqual( [4], player03.data)
