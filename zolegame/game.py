import random
from constansts import *
from rules import Rules

class BaseGame(object):

    def __init__(self, game_types, bet_size):
        self.game_types = game_types
        self.bet_size = bet_size
        self.players = []
        self.table_cards = []
        self.selected_game = None

    def addPlayers(self, playerA, playerB, playerC):
        self.players.append(playerA)
        self.players.append(playerB)
        self.players.append(playerC)

    def play(self):
        self.initNewGame()
        self._dealCards()
        self._selectContract()
        self._playTricks()
        card_points, trick_count = self._countPoints()
        player_points = self._countGamePoints(card_points, trick_count)
        for i in xrange(3):
            self.players[i].updatePoints(player_points[i])

    def initNewGame(self):
        for p in self.players:
            p.newGame()

    def _countGamePoints(self, card_points, trick_counts):
        player_points = [0, 0, 0]
        roles = [x.contract for x in self.players]
        small_points = 0
        if (Contract.TABLE in roles) or (Contract.BIG in roles):
            great_seat = roles.index(self.selected_game)
            small_tricks = sum(trick_counts) - trick_counts[great_seat]
            point_gain = 0
            if (Contract.BIG in roles):
                point_gain = 4
            great_points, small_points = Rules.countPartnerGamePoints(card_points[great_seat],
                                                point_gain,
                                                small_tricks)
            player_points[great_seat] = great_points

        if Contract.SMALL in roles:
            great_seat = roles.index(self.selected_game)
            if trick_counts[great_seat] != 0:
                player_points[great_seat] = -7 * 2
                small_points = 7
            else:
                player_points[great_seat] = 6 * 2
                small_points = -6

        if self.selected_game == Contract.DESK:
            max_tricks = [x if x == max(trick_counts) else 0 for x in trick_counts]
            max_trick_points = map(lambda x,y:x*y,max_tricks, card_points)
            looser = max_trick_points.index(max(max_trick_points))
            player_points[looser] = -2 * 2
            small_points = 2

        player_points = [x if x!=0 else small_points for x in player_points]
        return player_points

    def _countPoints(self):
        card_points = []
        trick_count = []
        for p in self.players:
            trickCount, points = Rules.countCardPoints(p.tricks)
            card_points.append(points)
            trick_count.append(trickCount)
        return card_points, trick_count

    def _playTricks(self):
        first = 0
        for i in xrange(len(self.players[0].cards)):
            second = Rules.nextPlayer(first)
            last = Rules.nextPlayer(second)
            first_index = self._playTrick([self.players[first].uuid,
                                                   self.players[second].uuid,
                                                   self.players[last].uuid])
            first = next(self.players.index(x)
                     for x in self.players
                     if x.uuid == first_index)

            # In small game: small player loose game on first winning trick
            if self.players[first].contract == Contract.SMALL:
                break

    def _selectContract(self, contracts = None):
        # Ask for game type and deside what to do with table cards

        for p in self.players:
            contract = p.selectContract(self.game_types)
            if contract not in self.game_types:
                raise IndentationError

            if contract == Contract.TABLE:  #Start normal Solo game with table cards
                self.selected_game = Contract.TABLE
                #Add table cards to solo player
                table = self.table_cards
                p.addCards(table)

                #Ask solo player to place 2 cards
                self._playTrick([p.uuid])
                self._playTrick([p.uuid])
                break

            if contract == Contract.BIG:  #Start Solo game without table cards
                self.selected_game = Contract.BIG
                break

            if contract == Contract.SMALL: #Start Null game when solo palyer cannot winn a trick
                self.selected_game = Contract.SMALL
                break

        if  self.selected_game == None:  #Start to table game the looser is with moust tricks
            if Contract.DESK in self.game_types:
                self.selected_game = Contract.DESK
            else:
                self.selected_game = Contract.PARTNER

    def _playTrick(self,player_list):
        trick =[]
        first_card = None
        for pIndex in player_list:
            p = next(x for x in self.players if x.uuid == pIndex)
            card = p.selectCard(first_card)
            trick.append(card)
            if first_card == None:
                first_card = card
        winner = player_list[Rules.bestCard(trick)]

        #Add trick cards to player
        for p in self.players:
            if p.uuid == winner:
                p.addTrick(trick)

        return winner

    def _dealCards(self, card_deck = None):
        #mix up the deck
        if card_deck == None:
            card_deck = list(Cards.ALL)
            random.shuffle(card_deck)

        for p in self.players:
            cards = card_deck[:8]
            del card_deck[:8]
            p.addCards(cards)

        self.table_cards = card_deck       #remaining cards to the table

    def sendToPlayers(self, except_player, message, data):
        for p in self.players:
            if p.uuid != except_player:
                p.sendToClient(message, data)
